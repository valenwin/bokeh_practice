# Titanic Survival Analysis with Bokeh

This project uses the Titanic dataset to create interactive visualizations of survival rates across different demographics using Bokeh.

## Project Description

The script generates three interactive Bokeh visualizations to explore various aspects of passenger survival on the Titanic:

1. Age Group Survival: A bar chart showing survival rates across different age groups.
2. Class and Gender Survival: A grouped bar chart comparing survival rates across different classes and genders.
3. Fare vs. Survival: A scatter plot with Fare on the x-axis and survival status on the y-axis, using different colors to represent different classes.

## Requirements

- Python 3.x
- pandas
- numpy
- bokeh

You can install the required packages using pip:

```
pip install -r requirements.txt
```

## Data

The analysis uses the 'titanic.csv' file, which should be placed in the same directory as the script. You can download this dataset from Kaggle: [Titanic Dataset](https://www.kaggle.com/c/titanic/data)

## Usage

1. Ensure all requirements are installed and the CSV file is in the correct location.
2. Run the script:

```
python task.py
```

3. The script will generate an HTML file named `titanic_survival_analysis.html` in the same directory.

## Visualizations

The generated HTML file contains three interactive visualizations:

1. Age Group Survival Bar Chart
2. Class and Gender Survival Bar Chart
3. Fare vs Survival Scatter Plot

The scatter plot includes filtering options for class and gender.

## Code Structure

- `preprocess_data()`: Handles missing values and creates necessary columns.
- `calculate_survival_rates()`: Calculates survival rates for grouped data.
- `age_group_survival_chart()`: Creates the age group survival bar chart.
- `class_gender_survival_chart()`: Creates the class and gender survival bar chart.
- `fare_survival_scatter_plot()`: Creates the fare vs survival scatter plot with interactive filters.

## Customization

You can modify the `preprocess_data()` function to change how missing values are handled or to create different age group categories.

## Output

The script will save an HTML file named `titanic_survival_analysis.html` in the same directory. Open this file in a web browser to interact with the visualizations.

## Author

Valentyna Lysenok

## Acknowledgements

- Titanic dataset provided by Kaggle
- Visualizations created using Bokeh library
