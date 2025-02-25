# simple-datadashboard
# Data Analysis Dashboard

A simple data analysis dashboard built with Python and Streamlit. This app allows you to upload CSV or Excel files, preview the data, view basic statistics, and generate detailed graphs along with key metrics (maximum, minimum, average, median, and mode) for selected numerical columns.

## Features

- **File Upload:** Supports CSV and Excel files.
- **Data Preview:** Displays the first few rows of your dataset.
- **Basic Statistics:** Provides an overview using Pandas' descriptive statistics.
- **Detailed Column Analysis:** Computes and shows:
  - Maximum value
  - Minimum value
  - Average (Mean)
  - Median
  - Mode
- **Visualizations:**
  - **Histogram:** Analyze the distribution of a selected numerical column.
  - **Box Plot:** Identify outliers and visualize data spread.
  - **Trend Line:** Observe trends over the dataset.

## Requirements

- Python 3.6 or later
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [openpyxl](https://pypi.org/project/openpyxl/) (for Excel file support)

## Installation

1. **Clone the Repository or Download the Source Code**

   ```bash
   git clone https://github.com/yourusername/data-analysis-dashboard.git
   cd data-analysis-dashboard
