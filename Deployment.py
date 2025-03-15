import streamlit as st
import pickle
import pandas as pd

st.title('Customer Churn Prediction Model')

st.write("""
Enter the customer details to predict the likelihood of churn.
""")

# Collecting customer details
age = st.number_input('Customer Age', min_value=0)
gender = st.selectbox('Gender', ['Male', 'Female'])
tenure = st.number_input('Customer Tenure (months)', min_value=0)
usage_frequency = st.number_input('Usage Frequency', min_value=0)
support_calls = st.number_input('Number of Support Calls', min_value=0)
payment_delay = st.number_input('Payment Delay (in days)', min_value=0)
subscription_type = st.selectbox('Subscription Type', ['Standard', 'Premium', 'Basic'])
contract_length = st.selectbox('Contract Length', ['Annual', 'Quarterly', 'Monthly'])
total_spend = st.number_input('Total Spend ($)', min_value=0.0)
last_interaction = st.number_input('Last Interaction')

# Encoding gender, subscription type, and contract length using the provided values
gender_encoded = 0.55477 if gender == 'Male' else 0.44523
subscription_encoded = {'Standard': 0.337743, 'Premium': 0.336692, 'Basic': 0.325564}[subscription_type]
contract_length_encoded = {'Annual': 0.393123, 'Quarterly': 0.390660, 'Monthly': 0.216217}[contract_length]

# Create a dataframe with input data
input_data = pd.DataFrame({
    'Age': [age],
    'Gender': [gender_encoded],
    'Tenure': [tenure],
    'Usage Frequency': [usage_frequency],
    'Support Calls': [support_calls],
    'Payment Delay': [payment_delay],
    'Subscription Type': [subscription_encoded],
    'Contract Length': [contract_length_encoded],
    'Total Spend': [total_spend],
    'Last Interaction': [last_interaction]
})

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Predict churn
if st.button('Predict Churn'):
    prediction = model.predict(input_data)
    if prediction == 1:
        st.write('This customer is likely to churn.')
    else:
        st.write('This customer is not likely to churn.')
