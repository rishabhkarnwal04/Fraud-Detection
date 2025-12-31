from sklearn.metrics import classification_report, roc_auc_score

def evaluate(model, X_test, y_test):
    # Predict labels
    preds = model.predict(X_test)

    # Predict probabilities
    probas = model.predict_proba(X_test)[:, 1]

    # Print classification metrics
    print(classification_report(y_test, preds))
    print('ROC-AUC:', roc_auc_score(y_test, probas))
