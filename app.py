import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import requests
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve, auc

st.title("🛡️ Fraud Detection Intelligence Platform")
if "token" not in st.session_state:
    st.session_state.token = None

if "token" not in st.session_state:
    st.sidebar.subheader("Authentication")

username = st.sidebar.text_input(
    "Username"
)

password = st.sidebar.text_input(
    "Password",
    type="password"
)

if "username" not in st.session_state:
    st.session_state.username = None

    st.sidebar.success(
        f"Logged in as: {st.session_state.username}"
    )

if st.sidebar.button("Logout"):

    st.session_state.token = None
    st.session_state.username = None

    st.rerun()

if st.sidebar.button("Login"):

    response = requests.post(
        f"{API_URL}/login",
        json={
            "username": username,
            "password": password
        }
    )

    result = response.json()

    if "access_token" in result:

        st.session_state.token = (
            result["access_token"]
        )
        
        st.session_state.username = username

        st.sidebar.success(
            "Login Successful"
        )

    else:

        st.sidebar.error(
            "Login Failed"
        )

    response = requests.get(
    f"{API_URL}/predictions",
    headers={
        "Authorization":
        f"Bearer {st.session_state.token}"
    }
)    

st.sidebar.title("Navigation")

st.sidebar.info("""
Fraud Detection Intelligence Platform

Model: Random Forest Classifier

Version: 1.0
""")

st.sidebar.markdown("### Model Performance")

col1, col2 = st.columns(2)

with col1:
    st.metric("Accuracy", "99.95%")
    st.metric("Precision", "93%")

with col2:
    st.metric("Recall", "88%")
    st.metric("F1 Score", "90%")

page = st.sidebar.selectbox(
    "Choose Page",
    [
        "Prediction Dashboard",
        "Prediction History",
        "Admin Dashboard"
    ]
)

API_URL = "https://fraud-detection-intelligence-platform-production.up.railway.app"
# ==========================
# Prediction Dashboard
# ==========================

if st.session_state.token is None:

    st.warning(
        "Please login first."
    )

    st.stop()

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

        # Remove target column before prediction
        if "Class" in df.columns:
            df_features = df.drop("Class", axis=1)
        else:
            df_features = df.copy()

        st.success("File Uploaded Successfully")

        st.subheader("Uploaded Data Preview")
        st.dataframe(df.head())

        response = requests.post(
            f"{API_URL}/predict-batch",
            json={
            "transactions": df_features.values.tolist()
            },
            headers={
            "Authorization":
            f"Bearer {st.session_state.token}"
            }
        )

        result = response.json()

        predictions = result["predictions"]
        fraud_probabilities = result["fraud_probabilities"]

        df["Prediction"] = predictions

        df["Fraud Probability (%)"] = [
            round(prob * 100, 2)
            for prob in fraud_probabilities
        ]

        st.subheader("Prediction Results")
        st.dataframe(df.head())

        st.subheader("Fraud Probability Distribution")

        fig_prob = px.histogram(
            df,
            x="Fraud Probability (%)",
            nbins=20,
            title="Fraud Probability Distribution"
        )

        st.plotly_chart(
            fig_prob,
            use_container_width=True
        )   

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

        genuine_count = (df["Prediction"] == 0).sum()
        fraud_count = (df["Prediction"] == 1).sum()

        fig = px.pie(
            names=["Genuine", "Fraud"],
            values=[genuine_count, fraud_count],
            title="Fraud vs Genuine Transactions"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.subheader("Top 10 High-Risk Transactions")

        top_risk_df = df.sort_values(
            by="Fraud Probability (%)",
            ascending=False
        ).head(10)

        risk_fig = px.bar(
            top_risk_df,
            x=top_risk_df.index,
            y="Fraud Probability (%)",
            title="Top 10 High-Risk Transactions"
        )

        st.plotly_chart(
            risk_fig,
            use_container_width=True
        )

        st.subheader("Fraud Probability Distribution")

        hist_fig = px.histogram(
            df,
            x="Fraud Probability (%)",
            nbins=20,
            title="Fraud Probability Distribution"
        )

        st.plotly_chart(
            hist_fig,
            use_container_width=True
        )

        csv = df.to_csv(index=False)

        st.download_button(
            label="Download Prediction Results",
            data=csv,
            file_name="fraud_predictions.csv",
            mime="text/csv"  
        )

        st.subheader("Confusion Matrix")

if "Class" in df.columns:

    cm = confusion_matrix(
        df["Class"],
        df["Prediction"]
    )

    fig_cm = px.imshow(
        cm,
        text_auto=True,
        title="Confusion Matrix",
        labels=dict(
            x="Predicted",
            y="Actual",
            color="Count"
        )
    )

    st.plotly_chart(
        fig_cm,
        use_container_width=True
    )

    st.subheader("ROC Curve Analysis")

if "Class" in df.columns:

    fpr, tpr, thresholds = roc_curve(
        df["Class"],
        fraud_probabilities
    )

    roc_auc = auc(
        fpr,
        tpr
    )

    fig_roc = px.area(
        x=fpr,
        y=tpr,
        title=f"ROC Curve (AUC = {roc_auc:.4f})",
        labels={
            "x": "False Positive Rate",
            "y": "True Positive Rate"
        }
    )

    st.plotly_chart(
        fig_roc,
        use_container_width=True
    )

    st.metric(
        "AUC Score",
        f"{roc_auc:.4f}"
    )

# ==========================
# Prediction History
# ==========================

if page == "Prediction History":

    st.header("Prediction History")

    response = requests.get(
        f"{API_URL}/predictions"
    )

    history_data = response.json()

    history_df = pd.DataFrame(history_data)

    if not history_df.empty:

       history_df["fraud_probability"] = (
        history_df["fraud_probability"] * 100
    ).round(2)
       
    history_df = history_df.rename(
    columns={
        "id": "ID",
        "prediction": "Prediction",
        "fraud_probability": "Fraud Probability (%)",
        "created_at": "Created At"
    }
)   

    history_df["Prediction"] = (
    history_df["Prediction"]
    .map({
        0: "Genuine",
        1: "Fraud"
    })
)

    history_df["Created At"] = pd.to_datetime(
    history_df["Created At"]
).dt.strftime(
    "%d %b %Y %I:%M %p"
)

    st.dataframe(history_df)

if page == "Admin Dashboard":

    st.header("Admin Dashboard")

    response = requests.get(
        f"{API_URL}/predictions",
        headers={
            "Authorization":
            f"Bearer {st.session_state.token}"
        }
    )

    data = response.json()

    admin_df = pd.DataFrame(data)

    if not admin_df.empty:

        total_predictions = len(admin_df)

        fraud_count = (
            admin_df["prediction"] == 1
        ).sum()

        genuine_count = (
            admin_df["prediction"] == 0
        ).sum()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Total Predictions",
                total_predictions
            )

        with col2:
            st.metric(
                "Fraud Transactions",
                fraud_count
            )

        with col3:
            st.metric(
                "Genuine Transactions",
                genuine_count
            )

        fig = px.pie(
            names=["Fraud", "Genuine"],
            values=[
                fraud_count,
                genuine_count
            ],
            title="Fraud vs Genuine"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
