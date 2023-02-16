# pypoll analysis
import os
import csv

import pandas as pd
pd.set_option('display.max_rows', 500)

election_file ='C:/Users/sikan/ub/homework/02_VBA/challenge_3/Instructions/PyPoll/Resources/election_data.csv'
# read csvfile
df = pd.read_csv(election_file )
    
# print header
header = df.columns
print(f'HEADER: {header}')

# no. of voters
voters_count = df['Ballot ID'].count()

print(f'VOTERS:{voters_count}')

#print(df)
#finding candidate names
candidates = df['Candidate'].unique()
print(candidates)

#counting number of votes for each candidate

candidate_1 = df['Candidate'].value_counts()['Charles Casper Stockham']
candidate_2 = df['Candidate'].value_counts()['Diana DeGette']
candidate_3 = df['Candidate'].value_counts()['Raymon Anthony Doane']

# finding percentage for each candidate 

p_1 = '%.3f'% ((candidate_1/ voters_count)*100)
p_2 = '%.3f'% ((candidate_2/ voters_count)*100)
p_3 = '%.3f'% ((candidate_3/ voters_count)*100)

# printing the results

print(p_1)
print(p_2)
print(p_3)
print(f'Charles Casper Stockham : votes ({candidate_1})   {p_1}% ')
print(f'Diana DeGette :votes ({candidate_2})  {p_2}%')
print(f'Raymon Anthony Doane :votes ({candidate_3})  {p_3}% ')

#finding winner
list1 = [23.049, 73.812, 3.139]
print(max(list1))

print(f'winner: Diana DeGette ')
print(max(list1))