import pandas as pd
import os


csvpath = r"C:\Users\bastaw1\PycharmProjects\GitHub\Python-Challenge\PyBank\budget_data.csv"
txtpath = r"C:\Users\bastaw1\PycharmProjects\GitHub\Python-Challenge\PyBank"

#Read csv file into pandas dataframe
df = pd.read_csv(csvpath)
#create variables and set to data required
totalrows = df['Date'].count()
totalprofit = df['Profit/Losses'].sum()
avgchng = round(df['Profit/Losses'].diff().mean(), 2)

# create helper column for month over month differences
df['Diff'] = round(df['Profit/Losses'].diff(), 1)
maxdiff = df['Diff'].max().astype(int)
mndiff = df['Diff'].min().astype(int)
mindate = df.loc[(df['Diff'] == mndiff),'Date'].values[0]
mxdate = df.loc[(df['Diff'] == maxdiff),'Date'].values[0]

#create list to hold lines to be added to text file and printed to terminal
line = [f"Financial Analysis ",f"--"*30,f"Total Months: {totalrows}",f"Total Profit: ${totalprofit}",f"Average Change: ${avgchng}",f"Greatest Increase in Profits: {mxdate} (${maxdiff})",f"Greatest Decrease in Profits: {mindate} (${mndiff})"]

#open text file from current directory and write lines to it
with open("budget_main.txt", "w") as text_file:
    for i in line:
        print(i)
        print(i, file = text_file)

os.startfile("budget_main.txt")


