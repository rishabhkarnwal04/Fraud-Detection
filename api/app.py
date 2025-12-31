from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()
model = joblib.load('fraud_model.pkl')

@app.post('/predict')
def predict(features: list):
features = np.array(features).reshape(1,-1)
prob = model.predict_proba(features)[0][1]
return {'fraud_probability': float(prob)}
