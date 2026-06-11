import pandas as pd

df = pd.read_csv("data/raw/creditcard.csv")

print(df.head())

print("\nShape of Dataset:")
print(df.shape)

print("\nFraud Distribution:")
print(df["Class"].value_counts())

fraud_percentage = (df["Class"].sum() / len(df)) * 100

print("\nFraud Percentage:")
print(f"{fraud_percentage:.4f}%")

print("\nMissing Values:")
print(df.isnull().sum().sum())

print("\nTransaction Amount Statistics:")
print(df["Amount"].describe())

print("\nFraud Transaction Amount Statistics:")
print(df[df["Class"] == 1]["Amount"].describe())

print("\nGenuine Transaction Amount Statistics:")
print(df[df["Class"] == 0]["Amount"].describe())

print("\nData Types:")
print(df.dtypes)

print("\nTime Statistics:")
print(df["Time"].describe())

print("\nClass Percentage:")
print(df["Class"].value_counts(normalize=True) * 100)

import matplotlib.pyplot as plt

df["Class"].value_counts().plot(kind="bar")

plt.title("Fraud vs Genuine Transactions")
plt.xlabel("Class")
plt.ylabel("Count")

plt.show()

import matplotlib.pyplot as plt

fraud_counts = df["Class"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(
    fraud_counts,
    labels=["Genuine", "Fraud"],
    autopct="%1.2f%%"
)

plt.title("Fraud vs Genuine Percentage")
plt.show()

print("\nAverage Amount by Class:")
print(df.groupby("Class")["Amount"].mean())

print("\nCorrelation with Fraud (Class):")
print(df.corr()["Class"].sort_values(ascending=False))

correlation = df.corr()["Class"].abs().sort_values(ascending=False)

print("\nTop 10 Features Related to Fraud:")
print(correlation.head(11))

import seaborn as sns
import matplotlib.pyplot as plt

top_features = [
    "Class",
    "V17",
    "V14",
    "V12",
    "V10",
    "V16",
    "V3",
    "V7",
    "V11",
    "V4",
    "V18"
]

plt.figure(figsize=(10, 8))

sns.heatmap(
    df[top_features].corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Top Fraud Features Correlation Heatmap")
plt.show()

plt.figure(figsize=(8,5))

sns.boxplot(
    x="Class",
    y="V17",
    data=df
)

plt.title("V17 Distribution by Class")
plt.show()

X = df.drop("Class", axis=1)
y = df["Class"]

print("\nFeature Matrix Shape:")
print(X.shape)

print("\nTarget Variable Shape:")
print(y.shape)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nX_train Shape:", X_train.shape)
print("X_test Shape:", X_test.shape)

print("\ny_train Shape:", y_train.shape)
print("y_test Shape:", y_test.shape)

print("\nTrain Class Distribution:")
print(y_train.value_counts(normalize=True) * 100)

print("\nTest Class Distribution:")
print(y_test.value_counts(normalize=True) * 100)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train["Amount"] = scaler.fit_transform(
    X_train[["Amount"]]
)

X_test["Amount"] = scaler.transform(
    X_test[["Amount"]]
)

print("\nAmount Scaling Complete")
print(X_train["Amount"].head())

print("\nScaled Amount Statistics:")
print(X_train["Amount"].describe())

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

print("\nLogistic Regression Training Complete")

y_pred = model.predict(X_test)

print("\nPredictions Complete")
print(y_pred[:10])

from sklearn.metrics import classification_report

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

rf_model.fit(X_train, y_train)

print("\nRandom Forest Training Complete")

rf_pred = rf_model.predict(X_test)

from sklearn.metrics import classification_report

print("\nRandom Forest Classification Report:")
print(classification_report(y_test, rf_pred))

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

print("\nAccuracy:")
print(accuracy_score(y_test, rf_pred))

print("\nPrecision:")
print(precision_score(y_test, rf_pred))

print("\nRecall:")
print(recall_score(y_test, rf_pred))

print("\nF1 Score:")
print(f1_score(y_test, rf_pred))

from sklearn.metrics import confusion_matrix

rf_cm = confusion_matrix(y_test, rf_pred)

print("\nRandom Forest Confusion Matrix:")
print(rf_cm)

feature_importance = rf_model.feature_importances_

importance_df = pd.DataFrame({
    "Feature": X_train.columns,
    "Importance": feature_importance
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

print("\nTop 10 Important Features:")
print(importance_df.head(10))

import matplotlib.pyplot as plt

top10 = importance_df.head(10)

plt.figure(figsize=(10, 6))

plt.barh(
    top10["Feature"],
    top10["Importance"]
)

plt.title("Top 10 Feature Importance")
plt.xlabel("Importance")

plt.gca().invert_yaxis()

plt.show()

from xgboost import XGBClassifier

xgb_model = XGBClassifier(
    n_estimators=100,
    max_depth=6,
    learning_rate=0.1,
    random_state=42,
    eval_metric="logloss"
)

xgb_model.fit(X_train, y_train)

print("\nXGBoost Training Complete")

xgb_pred = xgb_model.predict(X_test)

from sklearn.metrics import classification_report

print("\nXGBoost Classification Report:")
print(classification_report(y_test, xgb_pred))

rf_fraud_detected = (rf_pred == 1).sum()

print("\nFraud Transactions Predicted:")
print(rf_fraud_detected)

import joblib

joblib.dump(rf_model, "models/random_forest.pkl")

print("\nModel Saved Successfully")