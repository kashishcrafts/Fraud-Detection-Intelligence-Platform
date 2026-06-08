import joblib

model = joblib.load("models/random_forest.pkl")

print("Model Loaded Successfully")

print(type(model))

print(model.n_features_in_)

sample_transaction = [[0] * 30]

prediction = model.predict(sample_transaction)

print("Prediction:")
print(prediction)