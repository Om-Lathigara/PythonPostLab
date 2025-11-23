import pandas as pd
df = pd.read_excel('sample_data.xlsx')
df['Age'] = df['Age'].fillna(df['Age'].mean())
print(df)