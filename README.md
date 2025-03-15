# ChurnShield Predictor

## Overview
The Customer Churn Predictor is a machine learning project aimed at predicting whether customers are likely to discontinue using a company's services. By analyzing customer behavior and engagement, this tool helps businesses identify at-risk customers and take proactive measures to improve retention.

## Features
- **Churn Prediction:** Easily predict if a customer is likely to churn.
- **Insights:** View key factors influencing customer churn.
- **Data Analysis:** Analyze customer behavior based on various metrics.
- **Power BI Report:** Visualize customer data and churn insights through an interactive Power BI dashboard.

## Dataset
The project uses a dataset that includes the following features:
- `CustomerID`: Unique identifier for each customer
- `Age`: Age of the customer
- `Gender`: Gender of the customer
- `Tenure`: Duration in months for which a customer has been using the company's products
- `Usage Frequency`: Number of times the customer has used the service in the last month
- `Support Calls`: Number of calls made to customer support in the last month
- `Payment Delay`: Days the customer has delayed payment in the last month
- `Subscription Type`: Type of subscription chosen by the customer
- `Contract Length`: Duration of the contract
- `Total Spend`: Total amount spent by the customer
- `Last Interaction`: Days since the last interaction with the company
- `Churn`: Binary label indicating whether a customer has churned (1) or not (0)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/customer-churn-predictor.git
   cd customer-churn-predictor
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Power BI Report
In addition to the machine learning model, we have created an interactive Power BI report to visualize key insights about customer churn. The report includes:
- **Churn Rate Analysis:** Understand the overall churn rate and its distribution across different customer segments.
- **Customer Demographics:** Explore churn trends based on age, gender, and tenure.
- **Behavioral Metrics:** Analyze metrics like usage frequency, payment delays, and support calls.
- **Spending Patterns:** Visualize total spend and its correlation with churn.

### How to Access the Report
1. Download the Power BI report file (`CustomerChurnReport.pbix`) from the repository.
2. Open the file in Microsoft Power BI Desktop.
3. Connect the report to the dataset by following the instructions in the `README.md` file.
4. Explore the interactive visualizations to gain deeper insights into customer churn.

## Usage
1. Prepare your data by ensuring it matches the structure of the provided dataset.
2. Train the model using the training script:
   ```bash
   python train_model.py
   ```
3. Use the prediction script to generate churn predictions:
   ```bash
   python predict.py --input your_input_file.csv --output predictions.csv
   ```
4. Optionally, load your data into the Power BI report to explore additional insights.

## Technologies Used
- **Python**: For data preprocessing, model training, and prediction.
- **Pandas & NumPy**: For data manipulation and analysis.
- **Scikit-learn**: For building and evaluating the machine learning model.
- **Power BI**: For creating interactive visualizations and dashboards.

## Future Enhancements
- Add support for real-time churn prediction using APIs.
- Incorporate additional visualization tools like Tableau.
- Extend the Power BI report with more granular filters and predictive insights.
- Explore deep learning models for improved accuracy.



