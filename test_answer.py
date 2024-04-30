import seaborn as sns
import pandas as pd

# loc: "localizes" a label in the DataFrame.
# idxmax: takes the index of the occurrence of the maximum value of the group (in the case, df['passengers'])
df = pd.DataFrame(sns.load_dataset('flights'))
print(df.loc[df["passengers"].idxmax()])
# Other way to do it, but without the methods loc() and idxmax().
months_passengers = {}
passengers = df['passengers']
months = df['month']
for i in range(len(df)):
  months_passengers[passengers[i]] = months[i]
print(f'\nMonth: {months_passengers[max(passengers)]}'
f'\nPassengers: {max(passengers)}')
