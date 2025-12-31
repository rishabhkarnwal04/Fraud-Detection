from sklearn.ensemble import IsolationForest


def detect_anomalies(X):
iso = IsolationForest(contamination=0.02, random_state=42)
return (iso.fit_predict(X)==-1).astype(int)
