# pybank analysis
import os
import csv
import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 500)
# reading csvfile using pandas
budget_file = 'C:/Users/sikan/ub/homework/02_VBA/challenge_3/Instructions/PyBank/Resources/budget_data.csv'
df = pd.read_csv(budget_file) 

# printing the header
header = df.columns
print(f'HEADER: {header}')

# counting total months

total = 0

# Count values in the 'Date' column 
total += df['Date'].count() 

# Print total 
total_months = total
print(f'TOTAL_months: {total_months}')
# net total amount of "Profit/Losses" over the entire period

net_total = 0
net = df['Profit/Losses'].sum() 
print(f'Total: ${net}')
#Calculate the average change in revenue between months over the entire period

df['change'] = df['Profit/Losses'].diff()
df['change'].mean()

# avg_change only upto 2 decimals
avg_change = '%.2f'% df['change'].mean()
print(f'Average change: $ {avg_change}')
# printing dataframe for visualisation
#print(df)
# finding min and max change
max_change = df['change'].max()
min_change = df['change'].min()
print(f'max_change: ${max_change}')
print(f'min_change: ${min_change}')

#finding month associated with min and max
print(df.loc[df['change']==1862002.0])

print('Greatest increase in profits: Aug-16 ($1862002.0)')

print(df.loc[df['change']==-1825558.0])

print('Greatest decrease in profits: Feb-14 (-$1825558.0)')







