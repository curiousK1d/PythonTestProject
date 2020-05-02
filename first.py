import pandas as pd
import os

print(os.getcwd())
testdata = pd.read_csv('resources\\bank_full.csv')
print(testdata.head())
