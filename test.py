import matplotlib.pyplot as plt
import pandas as pd

filename = "data/trackLog-2022-Feb-20_18-45-32.csv"
df = pd.read_csv(filename, sep=',')
print(df.columns)
print(df.shape)

cols = [' Device Time', 'Kilometers Per Litre(Instant)(kpl)', 'Engine RPM(rpm)']
df[cols].to_csv('./debug.csv', sep=',', index=False)

# outliers
idx = df['Kilometers Per Litre(Instant)(kpl)'] >= 20
df.loc[idx, 'Kilometers Per Litre(Instant)(kpl)'] = 20

df['Kilometers Per Litre(Instant)(kpl)'].plot(label='kpl', color='red')
(df['Engine RPM(rpm)'] / 1000).plot(label='rpm', color='blue')

plt.legend()
plt.xlabel('Time')
plt.savefig('plot.png')
