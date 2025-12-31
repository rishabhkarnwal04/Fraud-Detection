from data.generate_data import generate_transactions
from preprocessing.preprocess import preprocess
from models.train_and_save import train_and_save
from evaluation.evaluate import evaluate
from anomaly.isolation_forest import detect_anomalies

# Generate data
df = generate_transactions()

# Preprocess
X_train, X_test, y_train, y_test = preprocess(df)

# Train & Save model
model = train_and_save(X_train, y_train)

# Evaluate
evaluate(model, X_test, y_test)

# Anomaly detection
anomalies = detect_anomalies(X_test)
print('Anomalies detected:', anomalies.sum())
