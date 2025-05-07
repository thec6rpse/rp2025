import pandas as pd

df = pd.read_csv('es_01-06-05-25.xlsx - Orders.csv')

for col in df.columns:
    df = df.drop_duplicates(subset=[col], keep='first')
    
df.to_csv('cleaned_orders.csv', index=False)
df.to_excel('cleaned_orders.xlsx', index=False)