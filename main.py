from data.generate_data import generate_transactions
from preprocessing.preprocess import preprocess
from models.train_and_save import train_and_save
from evaluation.evaluate import evaluate
from anomaly.isolation_forest import detect_anomalies
