import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

st.title("🛡️ Fraud Detection Intelligence Platform")

st.sidebar.title("Navigation")

st.sidebar.info("""
Fraud Detection Intelligence Platform

Model: Random Forest Classifier

Version: 1.0
""")

page = st.sidebar.selectbox(
    "Choose Page",
    ["Prediction Dashboard", "Prediction History"]
)

API_URL = "http://fastapi:8000"

if page == "Prediction Dashboard":

    st.markdown("""
    ### AI-Powered Fraud Detection Intelligence Platform

    Upload transaction data to detect potentially fraudulent transactions using a Machine Learning model.
    """)

    uploaded_file = st.file_uploader(
        "Upload Transaction CSV",
        type=["csv"]
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.success("File Uploaded Successfully")

        st.subheader("Uploaded Data Preview")
        st.dataframe(df.head())

        response = requests.post(
            f"{API_URL}/predict-batch",
            json={
                "transactions": df.values.tolist()
            }
        )

        predictions = response.json()["predictions"]

        df["Prediction"] = predictions

        st.subheader("Prediction Results")
        st.dataframe(df.head())

        fraud_count = (df["Prediction"] == 1).sum()
        genuine_count = (df["Prediction"] == 0).sum()

        total_transactions = len(df)

        fraud_percentage = (
            fraud_count / total_transactions
        ) * 100

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Fraud Transactions",
                fraud_count
            )

        with col2:
            st.metric(
                "Genuine Transactions",
                genuine_count
            )

        with col3:
            st.metric(
                "Fraud Percentage",
                f"{fraud_percentage:.2f}%"
            )

        fig, ax = plt.subplots()

        ax.pie(
            [genuine_count, fraud_count],
            labels=["Genuine", "Fraud"],
            autopct="%1.1f%%"
        )

        ax.set_title(
            "Fraud vs Genuine Transactions"
        )

        st.pyplot(fig)

        csv = df.to_csv(index=False)

        st.download_button(
            label="Download Prediction Results",
            data=csv,
            file_name="fraud_predictions.csv",
            mime="text/csv"
        )

if page == "Prediction History":

    st.header("Prediction History")

    response = requests.get(
        f"{API_URL}/predictions"
    )

    history_data = response.json()

    history_df = pd.DataFrame(history_data)

    st.dataframe(history_df)