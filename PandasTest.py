import pandas as pd

s1 = pd.Series([1, 2, 3, 4])
print("Series s1: \n" + str(s1))

# change series index
s2 = pd.Series({"a": 1, "b": 2, "c": 3})
print("Series s2: \n" + str(s2))

# Dataframe
dictin = {"name": ["manoj", "minal", "ashwini"], "marks": [10, 20, 30]}
df1 = pd.DataFrame(dictin)
print("Dataframe df1: \n" + str(df1))

# Get CSV file
df2 = pd.read_csv("resources//bank_full.csv")
print("\n Head: \n" + str(df2.head()))
print("\n Tail: \n" + str(df2.tail()))
print("\n Describe: \n" + str(df2.describe()))
print("\n iloc: \n" + str(df2.iloc[0:3, 0:2]))
print("\n loc: \n" + str(df2.loc[0:3, ("age", "duration")]))

# DataFrame filters
print("\n Age greater than 95 \n" + str(df2[df2["age"] > 95]))
df3 = df2[(df2["age"] > 65) & (df2["job"] == 'services')]
print("\n Job- Services and Age greater than 65: \n" + str(df3))
