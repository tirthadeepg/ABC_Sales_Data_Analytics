# ABC Sales Management and Analytics Dashboard

## Overview

The ABC Sales Management and Analytics Dashboard is a Python-based business application that enables users to manage sales records and generate analytical dashboards from sales data.

The system provides functionality to add and delete sales records dynamically from a CSV file and automatically generates visual reports and business insights using Pandas and Matplotlib.

This project demonstrates the practical application of:

* Object-Oriented Programming (OOP)
* CSV File Handling
* Data Analysis
* Data Visualization
* Business Reporting Automation

---

## Business Use Case

ABC Company receives monthly sales transactions from different regions and salespersons.

Manually maintaining records and analyzing performance can be time-consuming and inefficient.

This application allows users to:

1. View current sales records
2. Add new sales transactions
3. Delete existing sales transactions
4. Automatically update the CSV database
5. Generate business dashboards
6. Produce management summary reports

---

## Features

### Sales Record Management

* View existing sales records
* Add new sales transactions
* Delete sales transactions
* Automatically save changes to CSV

### Sales Analytics

* Revenue by Region
* Revenue by Salesperson
* Revenue by Product
* Units Sold by Category
* Total Revenue Calculation
* Total Orders Calculation

### Dashboard Generation

The dashboard contains four visualizations:

1. Revenue by Region
2. Revenue by Salesperson
3. Units Sold by Category
4. Revenue by Product

### Summary Report

The application displays:

* Total Orders Processed
* Total Revenue Generated
* Best Performing Region
* Top Salesperson
* Highest Revenue Product
* Most Sold Category

---

## Technologies Used

* Python
* Pandas
* Matplotlib

---

## Project Structure

ABC-Sales-Dashboard/

├── main.py

├── data_loader.py

├── csv_manager.py

├── sales_analyzer.py

├── dashboard_generator.py

├── ABC_SalesReport.csv

├── requirements.txt

└── README.md

---

## Object-Oriented Design

### DataLoader

Responsible for loading sales data from the CSV file.

### CSVManager

Responsible for:

* Displaying sales records
* Adding new sales transactions
* Deleting sales transactions
* Saving updates to CSV

### SalesAnalyzer

Responsible for:

* Revenue calculations
* Regional analysis
* Product analysis
* Salesperson analysis
* KPI generation

### DashboardGenerator

Responsible for:

* Creating visual dashboards
* Displaying management summaries

---

## Workflow

Sales CSV File

↓

Load Data

↓

Add/Delete Sales Records

↓

Update CSV File

↓

Analyze Sales Data

↓

Generate Dashboard

↓

Generate Summary Report

---

## How to Run

Install dependencies:

pip install -r requirements.txt

Run the application:

python main.py

---

## Future Enhancements

* Update existing sales records
* Export reports to Excel
* Export dashboard as PDF
* Interactive dashboards using Streamlit
* Sales forecasting using Machine Learning

---

## Author

Tirthadeep Ghosh

Python OOP Business Analytics Use Case Project
