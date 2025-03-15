import streamlit as st
import pandas as pd
import numpy as np
import pickle
from streamlit_option_menu import option_menu

# Load the model and mean/std values
model_filename = 'model(1).pkl'

with open(model_filename, 'rb') as file:
    model = pickle.load(file)

with open('mean_std_values.pkl', 'rb') as f:
    mean_std_values = pickle.load(f)
st.set_page_config(page_title="Customer Churn", layout="wide")

# 1. Define the Home page
def home_page():
    outer_col1, outer_col2, outer_col3 = st.columns([1, 5, 1])
    with outer_col2:
        with st.container():
            col1, col2 = st.columns([2.5, 1])
            with col1:
                st.header("About this app", anchor=None)
                st.markdown(
                    "<div style='font-size:22px;'>- Easily predict if a customer is likely to churn or not using our <span style='color:red;'>Customer Churn Predictor</span>.<br>"
                    "- View customer churn behavior using our <span style='color:red;'>Insights</span>.</div>",
                    unsafe_allow_html=True
                )
            with col2:
                st.image("Header - Voluntary vs.png", width=400)

        with st.container():
            col1, col2 = st.columns([1, 1])
            with col1:
                st.header("What is customer churn?")
                st.write(
                    "<div style='font-size:20px;'>Customer churn occurs when customers stop using a company's products. This can result from various factors. "
                    "Customer features like ratings and usage metrics provide insight into customer behavior, especially when they're about to churn.</div>",
                    unsafe_allow_html=True
                )
            with col2:
                st.header("Why predict customer churn?")
                st.write(
                    "<div style='font-size:20px;'>It's much more expensive to acquire new customers than to retain existing ones. "
                    "Predicting customer churn and identifying early warning signs can save significant costs for a company.</div>",
                    unsafe_allow_html=True
                )

        
        st.markdown("<hr style='border: 2px solid gray;'>", unsafe_allow_html=True)

        
        st.markdown("<h2 style='text-align: center;'>About Dataset</h2>", unsafe_allow_html=True)

        st.write(
            "<div style='font-size:18px; text-align: justify;padding: 20px;'>The churn label indicates whether a customer has churned or not. A churned customer is one who has decided to discontinue their subscription or usage of the company's services. On the other hand, a non-churned customer is one who continues to remain engaged and retains their relationship with the company.</div>",
            unsafe_allow_html=True
        )
        st.write(
            "<div style='font-size:18px; text-align: justify;padding: 20px;'>The dataset includes customer information such as age, gender, tenure, usage frequency, support calls, payment delay, "
            "subscription type, contract length, total spend, and last interaction details. This information is used to predict whether a customer is likely to churn based on these behaviors.</div>",
            unsafe_allow_html=True
        )
        st.write(
    "<div style='font-size:18px; text-align: justify; padding: 20px;'>"
    "These datasets contain 12 feature columns. In detail, these are:<br><br>"
    "<ul>"
    "<li><b>CustomerID:</b> A unique identifier for each customer</li>"
    "<li><b>Age:</b> The age of the customer</li>"
    "<li><b>Gender:</b> Gender of the customer</li>"
    "<li><b>Tenure:</b> Duration in months for which a customer has been using the company's products or services</li>"
    "<li><b>Usage Frequency:</b> Number of times the customer has used the company’s services in the last month</li>"
    "<li><b>Support Calls:</b> Number of calls the customer has made to customer support in the last month</li>"
    "<li><b>Payment Delay:</b> Number of days the customer has delayed their payment in the last month</li>"
    "<li><b>Subscription Type:</b> Type of subscription the customer has chosen</li>"
    "<li><b>Contract Length:</b> Duration of the contract the customer has signed with the company</li>"
    "<li><b>Total Spend:</b> Total amount of money the customer has spent on the company's products or services</li>"
    "<li><b>Last Interaction:</b> Number of days since the last interaction the customer had with the company</li>"
    "<li><b>Churn:</b> Binary label indicating whether a customer has churned (1) or not (0)</li>"
    "</ul>"
    "</div>",
    unsafe_allow_html=True
)

# 2. Define the Prediction page
def predict_page():
    outer_col1, outer_col2, outer_col3 = st.columns([1, 5, 1])
    with outer_col2:
        # Add image centered
        with st.container():
            col1, col2, col3 = st.columns([1, 6, 1])
            with col2:
                st.image("image.png", use_column_width=True)

        st.title('Customer Behavior Prediction')

        # Input fields for the user to enter data
        st.header("Enter Customer Details:")
        age = st.number_input("Age", min_value=0, max_value=120, value=30)
        gender = st.selectbox("Gender", ["Male", "Female"])
        tenure = st.number_input("Tenure (Months)", min_value=0, max_value=100, value=12)
        usage_frequency = st.number_input("Usage Frequency (Last Month)", min_value=0, max_value=100, value=10)
        support_calls = st.number_input("Support Calls (Last Month)", min_value=0, max_value=50, value=3)
        payment_delay = st.number_input("Payment Delay (Days)", min_value=0, max_value=100, value=5)
        subscription_type = st.selectbox("Subscription Type", ["Standard", "Premium", "Basic"])
        contract_length = st.selectbox("Contract Length", ["Monthly", "Annual", "Quarterly"])
        total_spend = st.number_input("Total Spend", min_value=0.0, value=500.0, step=0.1)
        last_interaction = st.number_input("Last Interaction (Days)", min_value=0, max_value=100, value=20)

        # Convert categorical features to numerical
        gender_dict = {"Male": 1, "Female": 0}
        subscription_dict = {"Standard": 2, "Premium": 1, "Basic": 0}
        contract_dict = {"Monthly": 1, "Annual": 0, "Quarterly": 2}

        gender_val = gender_dict[gender]
        subscription_val = subscription_dict[subscription_type]
        contract_val = contract_dict[contract_length]

        # Prepare the input data
        input_data = np.array([age, gender_val, tenure, usage_frequency, support_calls, 
                               payment_delay, subscription_val, contract_val, 
                               total_spend, last_interaction]).reshape(1, -1)

        # Normalize the input data
        input_data = (input_data - mean_std_values['mean']) / mean_std_values['std']

        # Add the predict button
        if st.button('Predict'):
            # Perform the prediction
            prediction = model.predict(input_data)
            prediction_proba = model.predict_proba(input_data)

            if prediction[0] == 1:
                bg_color = 'red'
                prediction_result = 'The customer has churned'
            else:
                bg_color = 'green'
                prediction_result = 'The customer has not churned'

            confidence = prediction_proba[0][1] if prediction[0] == 1 else prediction_proba[0][0]

            # Display the result
            st.markdown(f"<p style='background-color:{bg_color}; color:white; padding:15px; font-size:18px;'>Prediction: {prediction_result}<br>Confidence: {((confidence*10000)//1)/100}%</p>", unsafe_allow_html=True)


# 3. Define the Insights page (Placeholder for visuals)
def insights_page():
    outer_col1, outer_col2, outer_col3 = st.columns([1, 5, 1])
    with outer_col2:
        with st.container():
            st.header("Customer Churn Behavior Analysis")
            st.write("In this section, you can view visual insights regarding customer churn behavior.")
             
            st.markdown("<hr style='border: 2px solid gray;'>", unsafe_allow_html=True)
            # First plot with description
            st.subheader("1. Distribution of customer's gender")
            col1, col2 = st.columns([2.5, 1])
            with col1:
                st.write("""
                    There are more male customers in the company./
                """)
            with col2:
                st.image("visualization/Gender.PNG", width=400)

            # Second plot with description
            st.subheader("2. Distribution of customer's subscription type")
            col1, col2 = st.columns([2.5, 1])
            with col1:
                st.write("""
                    There is a close balance of customers among the three subscription types: Standard, Premium, and Basic.
                """)
            with col2:
                st.image("visualization/customer subscription.PNG", width=400)

            # Third plot with description
            st.subheader("3. Distribution of customer's contract length")
            col1, col2 = st.columns([2.5, 1])
            with col1:
                st.write("""
                    Annual and quarterly contracts have similar and the highest number of customer counts, followed by monthly contracts with the lowest number of customers.
                """)
            with col2:
                st.image("visualization/Contract.PNG", width=400)
                
                
                # Third plot with description
            st.subheader("4. Distribution of cutomer's age (years)")
            col1, col2 = st.columns([2.5, 1])
            with col1:
                st.write("""
                    Most customers are aged 40-50 with age 50 being the most common. There's very low number of customers of age 51 and above.
                """)
            with col2:
                st.image("visualization/Age.PNG", width=500)
                
               # Third plot with description
            st.subheader("5. Distribution of cutomer's support_calls")
            col1, col2 = st.columns([2.5, 1])
            with col1:
                st.write("""
                    On average, customers tend to make 3 support calls in a month. Customers tend to make 1 or 2 support calls per month, with the most make no support calls at all.
                """)
            with col2:
                st.image("visualization/calls.PNG", width=500)
              # Third plot with description
            st.subheader("6. Gender wise churn rate")
            col1, col2 = st.columns([2.5, 1])
            with col1:
                st.write("""
                    gender and churn rate have relationship.

                female customers exhibit a slightly higher churn rate compared to male customers. Active male customers (non-churned) is nearly double that of female customers.
                """)
            with col2:
                st.image("visualization/gender1.PNG", width=500)  
            
            # Third plot with description
            st.subheader("7. Churn rate based on payment delays")
            col1, col2 = st.columns([2.5, 1])
            with col1:
                st.write("""
                    Customers who are not churned tend to have higher payment delay days as compared with churned customers till day 20, after which churned customers have payment delays just over 10 times than that of not churned customers.
                """)
            with col2:
                st.image("visualization/delay.PNG", width=500)  
                 
            # Third plot with description
            st.subheader("8. Churn rate based on tenures")
            col1, col2 = st.columns([2.5, 1])
            with col1:
                st.write("""
                    customers with longer tenures are more likely to churn
                """)
            with col2:
                st.image("visualization/tenur.PNG", width=520)  
                 
             # Third plot with description
            st.subheader("9. Customer Support Calls")
            col1, col2 = st.columns([2.5, 1])
            with col1:
                st.write("""
                    Customers with more support calls tend to churn more.

                   On the contrary, customers who are not churned tend to make much more 0 to 3 customer support calls than churned customers, after which churned customers make significantly more calls.
                """)
            with col2:
                st.image("visualization/support.PNG", width=500)     
            
            # Third plot with description
            st.subheader("10. Churn rate based on subscription type")
            col1, col2 = st.columns([2.5, 1])
            with col1:
                st.write("""The subscription type does not influence customer churn rate.

Customers who are not churned tend to choose premium or standard subscription type slightly more than basic subscription.
                                      
                """)
            with col2:
                st.image("visualization/type.PNG", width=500)  
            
            # Third plot with description
            st.subheader("11. Churn rate based on contract length")
            col1, col2 = st.columns([2.5, 1])
            with col1:
                st.write("""
                     Customers with quarterly contract lengths have the lowest churn rate, while those with monthly contract lengths exhibit the highest churn rate. Conversely, customers who do not churn overwhelmingly prefer annual and quarterly contracts over monthly contracts.
                """)
            with col2:
                st.image("visualization/contractlen.PNG", width=500)   
                
            # Third plot with description
            st.subheader("12. correlation between total spend and churn rate")
            col1, col2 = st.columns([2.5, 1])
            with col1:
                st.write("""
                     Customers who churn tends to spend significantly more money than those who don't.

Both churn and not churned customers share common total spending distribution / total spending behavior.
                """)
            with col2:
                st.image("visualization/spend.PNG", width=500)  
                
             # Third plot with description
            st.subheader("13. Correlation Heatmap between Independent Features and Churn")
            col1, col2 = st.columns([2.5, 1])
            with col1:
                st.write("""
                     Support Calls (0.52): This has the strongest positive correlation with churn. As the number of support calls increases, the likelihood of churn also increases. This indicates that customers who need more support are more likely to leave, possibly due to dissatisfaction.

Payment Delay (0.33): There is a moderate positive correlation between payment delay and churn. Customers who delay their payments are more likely to churn, suggesting financial instability or dissatisfaction with the service.

Last Interaction (0.13): A weak positive correlation, implying that customers who interact with the company after a long time might be at a slightly higher risk of churn.

Age (0.19): There is a weak positive correlation with churn, meaning older customers may be somewhat more likely to churn compared to younger ones.

Usage Frequency (-0.053): This has a weak negative correlation, suggesting that customers who use the service frequently are slightly less likely to churn.

Total Spend (-0.37): A moderate negative correlation indicates that customers who spend more are less likely to churn. High spenders may derive more value from the service, making them more loyal.

Tenure (-0.021): A very weak negative correlation, suggesting that how long a customer has been with the company has almost no impact on churn.
                """)
            with col2:
                st.image("visualization/correlation.PNG", width=700)                       
            



# 4. Upper navbar to navigate between pages
selected = option_menu(
    menu_title=None,
    options=["Home", "Insights", "Predict"],  
    icons=["house", "graph-up-arrow", "bar-chart-line"],  
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#f8f9fa"},
        "nav-link": {
            "font-size": "20px",
            "text-align": "center",
            "margin": "0px",
            "width": "100%",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "#0d6efd"}, 
    }
)

# 5. Render the selected page
if selected == "Home":
    home_page()
elif selected == "Predict":
    predict_page()
elif selected == "Insights":
    insights_page()
