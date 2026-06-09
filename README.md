# COVID-19 Data Analysis

## Project Overview

This project analyzes COVID-19 trends using country-wise time-series data. The analysis focuses on understanding daily cases, rolling averages, peak detection, and comparisons between multiple countries.

## Objectives

- Load and analyze COVID-19 time-series data
- Calculate daily COVID-19 cases
- Compute 7-day rolling averages
- Compare trends across countries
- Detect peak infection periods
- Generate visual reports and insights

## Dataset

The dataset contains country-wise COVID-19 statistics including:

- Date
- Country
- New Cases
- Total Cases

Countries analyzed:

- India
- United States
- Brazil

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib

## Project Structure

```text
Syntecxhub_COVID19_Analysis/
│
├── data/
│   └── covid_data.csv
│
├── outputs/
│   ├── daily_cases.png
│   ├── rolling_average.png
│   ├── country_comparison.png
│   └── peaks.png
│
├── main.py
├── insights.txt
├── requirements.txt
└── README.md
```

## Visualizations Generated

### 1. Daily Cases Analysis
Displays daily COVID-19 cases for selected countries.

### 2. Rolling Average Analysis
Shows 7-day rolling averages to smooth daily fluctuations.

### 3. Country Comparison
Compares total COVID-19 cases among countries.

### 4. Peak Detection
Identifies the highest daily case counts recorded by each country.

## Key Findings

- The United States recorded the highest peak daily cases.
- India experienced rapid case growth during major waves.
- Brazil maintained prolonged high infection periods.
- Rolling averages provided a clearer representation of trends than raw daily data.

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

## Output

The generated visualizations are automatically saved in the `outputs` folder.

## Internship Task

Week 3 Data Science Internship Project

Project: COVID-19 Data Analysis

Submitted as part of the Syntecxhub Internship Program.