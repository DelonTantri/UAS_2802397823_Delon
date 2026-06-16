import streamlit as st
from inference import CreditScoreInference

predictor = CreditScoreInference()


st.set_page_config(
    page_title="Credit Score Classification",
    page_icon="💳",
    layout="wide"
)

st.title("Credit Score Classification")

st.markdown("""
Masukkan informasi keuangan pelanggan untuk
memprediksi kategori **Credit Score**.

Model:
- Random Forest
- Accuracy: 73.86%
- Weighted F1 Score: 73.68%
""")

# input form
col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30
    )

    annual_income = st.number_input(
        "Annual Income",
        min_value=0.0,
        value=50000.0
    )

    bank_accounts = st.number_input(
        "Number of Bank Accounts",
        min_value=0,
        value=5
    )

    credit_cards = st.number_input(
        "Number of Credit Cards",
        min_value=0,
        value=3
    )

    interest_rate = st.number_input(
        "Interest Rate",
        min_value=0.0,
        value=10.0
    )

with col2:

    num_loans = st.number_input(
        "Number of Loans",
        min_value=0,
        value=2
    )

    outstanding_debt = st.number_input(
        "Outstanding Debt",
        min_value=0.0,
        value=1000.0
    )

    credit_history_age = st.number_input(
        "Credit History Age (Months)",
        min_value=0,
        value=120
    )

    payment_min = st.selectbox(
        "Payment of Minimum Amount",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

# Predict button
if st.button(
    "Predict Credit Score",
    use_container_width=True
):

    user_data = {

        "Age": age,
        "Annual_Income": annual_income,
        "Num_Bank_Accounts": bank_accounts,
        "Num_Credit_Card": credit_cards,
        "Interest_Rate": interest_rate,
        "Num_of_Loan": num_loans,
        "Outstanding_Debt": outstanding_debt,
        "Credit_History_Age": credit_history_age,
        "Payment_of_Min_Amount": payment_min
    }

    prediction = predictor.predict(
        user_data
    )

    st.divider()

    if prediction == "Good":

        st.success(
            f"Predicted Credit Score: {prediction}"
        )

    elif prediction == "Standard":

        st.warning(
            f"Predicted Credit Score: {prediction}"
        )

    else:

        st.error(
            f"Predicted Credit Score: {prediction}"
        )