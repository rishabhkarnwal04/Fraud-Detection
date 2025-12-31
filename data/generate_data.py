import numpy as np
import pandas as pd


def generate_transactions(n=20000):
np.random.seed(42)
df = pd.DataFrame({
'transaction_id': range(1, n + 1),
'customer_id': np.random.randint(1000, 6000, n),
'amount': np.round(np.random.exponential(2500, n), 2),
'transaction_hour': np.random.randint(0, 24, n),
'merchant_risk': np.random.choice([0,1], n, p=[0.9,0.1]),
'is_international': np.random.choice([0,1], n, p=[0.85,0.15])
})
df['is_fraud'] = ((df['amount']>9000) | ((df['merchant_risk']==1) & (df['amount']>3000)) | ((df['is_international']==1) & (df['transaction_hour'].isin([1,2,3,4])))).astype(int)
return df
