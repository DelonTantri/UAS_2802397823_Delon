import json
import os

import boto3
import streamlit as st

from botocore.exceptions import (
    ClientError,
    NoCredentialsError
)


ENDPOINT_NAME = os.environ.get(
    "ENDPOINT_NAME",
    "credit-score-endpoint"
)

REGION = os.environ.get(
    "AWS_REGION",
    "us-east-1"
)


@st.cache_resource
def get_runtime_client():

    return boto3.client(
        "sagemaker-runtime",
        region_name=REGION
    )


def invoke_endpoint(features):

    runtime = get_runtime_client()

    payload = {
        "instances": [features]
    }

    response = runtime.invoke_endpoint(

        EndpointName=ENDPOINT_NAME,

        ContentType="application/json",

        Accept="application/json",

        Body=json.dumps(payload)
    )

    return json.loads(
        response["Body"].read().decode("utf-8")
    )


st.title(
    "Credit Score Classification"
)

st.write(
    "Predict Credit Score using AWS SageMaker Endpoint"
)

age = st.number_input(
    "Age",
    value=30
)

income = st.number_input(
    "Annual Income",
    value=50000.0
)

salary = st.number_input(
    "Monthly Salary",
    value=4000.0
)

bank_accounts = st.number_input(
    "Bank Accounts",
    value=5
)

cards = st.number_input(
    "Credit Cards",
    value=3
)

interest = st.number_input(
    "Interest Rate",
    value=10.0
)

loans = st.number_input(
    "Number of Loans",
    value=2
)

delay = st.number_input(
    "Delay From Due Date",
    value=5
)

delayed_payment = st.number_input(
    "Delayed Payments",
    value=2
)

changed_limit = st.number_input(
    "Changed Credit Limit",
    value=5.0
)

inquiries = st.number_input(
    "Credit Inquiries",
    value=3
)

debt = st.number_input(
    "Outstanding Debt",
    value=1000.0
)

utilization = st.number_input(
    "Credit Utilization Ratio",
    value=30.0
)

history = st.number_input(
    "Credit History Age",
    value=120
)

payment_min = st.selectbox(
    "Payment of Minimum Amount",
    [0,1]
)

emi = st.number_input(
    "Total EMI",
    value=200.0
)

invested = st.number_input(
    "Amount Invested Monthly",
    value=500.0
)

balance = st.number_input(
    "Monthly Balance",
    value=3000.0
)

if st.button(
    "Predict Credit Score"
):

    features = [
        age,
        income,
        salary,
        bank_accounts,
        cards,
        interest,
        loans,
        delay,
        delayed_payment,
        changed_limit,
        inquiries,
        debt,
        utilization,
        history,
        payment_min,
        emi,
        invested,
        balance
    ]

    try:

        result = invoke_endpoint(
            features
        )

        label = result["labels"][0]

        st.success(
            f"Predicted Credit Score: {label}"
        )

    except NoCredentialsError:

        st.error(
            "AWS credentials not found."
        )

    except ClientError as e:

        st.error(
            str(e)
        )
