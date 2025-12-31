from xgboost import XGBClassifier
import joblib

def train_and_save(X_train, y_train, path='fraud_model.pkl'):
    # Initialize XGBoost classifier
    model = XGBClassifier(
        n_estimators=300,
        max_depth=6,
        learning_rate=0.05,
        scale_pos_weight=10,
        eval_metric='logloss'
    )

    # Train the model
    model.fit(X_train, y_train)

    # Save the trained model
    joblib.dump(model, path)

    return model
