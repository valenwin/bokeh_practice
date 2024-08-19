import pandas as pd
from bokeh.io import output_file, save
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure
from bokeh.transform import dodge, factor_cmap

df = pd.read_csv('data/Titanic-Dataset.csv')


# Data preprocessing
def preprocess_data(df):
    df['Age'].fillna(df['Age'].median(), inplace=True)
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
    df.drop('Cabin', axis=1, inplace=True)

    df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 12, 18, 60, 100], labels=['Child', 'Teen', 'Adult', 'Senior'])
    df['Survived'] = df['Survived'].astype(int)

    return df


df = preprocess_data(df)


# Calculate survival rates
def calculate_survival_rates(group):
    return pd.DataFrame({
        'SurvivalRate': [group['Survived'].mean()],
        'Count': [len(group)]
    }, index=[group.name])


# Age Group Survival Bar Chart
def age_group_survival_chart(df):
    age_survival = df.groupby('AgeGroup').apply(calculate_survival_rates).reset_index()
    source = ColumnDataSource(age_survival)

    p = figure(x_range=age_survival['AgeGroup'].tolist(), height=350, title="Survival Rates by Age Group",
               toolbar_location=None, tools="")

    p.vbar(x='AgeGroup', top='SurvivalRate', width=0.9, source=source)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.y_range.end = 1
    p.yaxis.axis_label = 'Survival Rate'

    hover = HoverTool(tooltips=[
        ("Age Group", "@AgeGroup"),
        ("Survival Rate", "@SurvivalRate{0.2f}"),
        ("Count", "@Count"),
    ])
    p.add_tools(hover)

    return p


# Class and Gender Survival Bar Chart
def class_gender_survival_chart(df):
    class_gender_survival = df.groupby(['Pclass', 'Sex']).apply(calculate_survival_rates).reset_index()
    class_gender_survival['PclassStr'] = class_gender_survival['Pclass'].astype(str)
    source = ColumnDataSource(class_gender_survival)

    p = figure(x_range=['1', '2', '3'], height=350, title="Survival Rates by Class and Gender",
               toolbar_location=None, tools="")

    p.vbar(x=dodge('PclassStr', -0.25, range=p.x_range), top='SurvivalRate', width=0.2, source=source,
           color="#c9d9d3", legend_label="Female", name="Female")

    p.vbar(x=dodge('PclassStr', 0.0, range=p.x_range), top='SurvivalRate', width=0.2, source=source,
           color="#718dbf", legend_label="Male", name="Male")

    p.x_range.range_padding = 0.1
    p.xgrid.grid_line_color = None
    p.legend.location = "top_right"
    p.legend.orientation = "horizontal"
    p.xaxis.axis_label = 'Passenger Class'
    p.yaxis.axis_label = 'Survival Rate'

    hover = HoverTool(tooltips=[
        ("Class", "@PclassStr"),
        ("Gender", "$name"),
        ("Survival Rate", "@SurvivalRate{0.2f}"),
        ("Count", "@Count"),
    ])
    p.add_tools(hover)

    return p


# Fare vs Survival Scatter Plot
def fare_survival_scatter_plot(df):
    source = ColumnDataSource(df)

    p = figure(height=350, title="Fare vs Survival", toolbar_location=None, tools="")

    p.circle('Fare', 'Survived', size=5, source=source,
             color=factor_cmap('Pclass', 'Category10_3', ['1', '2', '3']))

    p.xaxis.axis_label = 'Fare'
    p.yaxis.axis_label = 'Survived'

    hover = HoverTool(tooltips=[
        ("Passenger", "@Name"),
        ("Fare", "@Fare"),
        ("Survived", "@Survived"),
        ("Class", "@Pclass"),
    ])
    p.add_tools(hover)

    return p


if __name__ == "__main__":
    age_chart = age_group_survival_chart(df)
    class_gender_chart = class_gender_survival_chart(df)
    fare_scatter = fare_survival_scatter_plot(df)

    output_file("titanic_survival_analysis.html")
    save(column(age_chart, class_gender_chart, fare_scatter))

    print("HTML file has been generated and saved as titanic_survival_analysis.html")
