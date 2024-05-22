# Real Estate Analysis Application

## Overview

The Real Estate Analysis Application is a comprehensive tool for analyzing real estate market data. It provides functionalities for data loading, analysis, visualization, model training, and report generation. The application uses various machine learning algorithms and data visualization techniques to help users gain insights from their real estate data.

## Features

- **Data Loading**: Load real estate data from a CSV file.
- **Data Analysis**: Perform basic statistical analysis on the loaded data.
- **Model Training**: Train Linear Regression and Random Forest models to predict real estate prices.
- **Classification**: Train a classifier to categorize properties.
- **Association Rule Analysis**: Perform association rule mining on the data.
- **Data Visualization**: Visualize data using interactive plots and maps.
- **PDF Report Generation**: Generate detailed PDF reports of the analysis results.
- **Data Editing**: View and edit the loaded data within the application.

## Requirements

- Python 3.x
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Tkinter
- Mlxtend
- Plotly
- ReportLab

## Installation

Clone the repository:
    ```sh
    git clone https://github.com/yourusername/real-estate-analysis-app.git
    cd real-estate-analysis-app
    ```
    
### Using setup.py

Install the package using `setup.py`:
    ```sh
    python setup.py install
    ```

### Using requirements.txt

Install the required Python libraries using `requirements.txt`:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    cd src
    python main.py
    ```

2. Load your real estate data by browsing for a CSV file.

3. Use the menu options to perform various analyses, visualize data, train models, and generate reports.

## Functionality Details

### Data Loading
- **Browse and Load Data**: Select and load data from a CSV file into the application.

### Data Analysis
- **Analyze Data**: Perform basic descriptive statistics on the loaded data.
- **Train Linear Model**: Train a Linear Regression model to predict property prices.
- **Train Random Forest Regressor**: Train a Random Forest model for price prediction.
- **Classify Properties**: Train a classifier to categorize properties based on features.
- **Association Rule Analysis**: Identify interesting associations and relationships within the data.

### Data Visualization
- **Visualize Data**: Generate various plots and interactive maps to visualize the real estate data.
- **Map Visualization**: Display properties on an interactive map using latitude and longitude coordinates.

### Report Generation
- **Generate PDF Report**: Create a comprehensive PDF report containing summary statistics, visualizations, and analysis results.

### Data Editing
- **View and Edit Data**: Open a new window to view and edit the data directly within the application.
