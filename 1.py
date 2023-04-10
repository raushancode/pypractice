import pandas as pd

import os

file_path = os.path.join(os.getcwd(),"bank/dataset/Kidwai Sep.csv")

df = pd.read_csv(file_path)
print(df.head(10))

print(df[['CUSTOMER_NAME', 'MODULE_SERIAL']])
