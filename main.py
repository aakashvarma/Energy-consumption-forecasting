import os
import pandas as pd

data_dir = "D:\Coding"
os.chdir(data_dir)

data_file = 'household_power_consumption.txt'
df = pd.read_csv(data_file, delimiter = ';')

print (df.head())
























