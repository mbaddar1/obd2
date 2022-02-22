import pandas as pd
filename = "data/trackLog-2022-Feb-20_18-45-32.csv"
df = pd.read_csv(filename,sep=',')
print(df.columns)
print(df.shape)