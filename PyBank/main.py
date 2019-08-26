import pandas as pd
import csv
import os

csvpath = r"C:\Users\bastaw1\PycharmProjects\GitHub\Python-Challenge\PyBank\budget_data.csv"
txtpath = r"C:\Users\bastaw1\PycharmProjects\GitHub\Python-Challenge\PyBank\budget_main.txt"

# def budget(budgetcsv):
#     date = budgetcsv[0]
#     value = budgetcsv[1]
#     totalrows = len(date)
#     totalprofit = 0
#     for profits in value:
#         totalprofit += profits
#     avg = totalprofit/totalrows

#
# with open('budget_data.csv','r') as budget
#     budgetcsv = csv.reader(budget, delimiter = ',')
# header = next(budgetcsv)

df = pd.read_csv(csvpath)

totalrows = df['Date'].count()
totalprofit = df['Profit/Losses'].sum()
avgchng = round(df['Profit/Losses'].diff().mean(), 2)

df['Diff'] = round(df['Profit/Losses'].diff(), 1)
maxdiff = df['Diff'].max().astype(int)
mndiff = df['Diff'].min().astype(int)
mindate = df.loc[(df['Diff'] == mndiff),'Date'].values[0]
mxdate = df.loc[(df['Diff'] == maxdiff),'Date'].values[0]

line = [f"Financial Analysis ",f"--"*30,f"Total Months: {totalrows}",f"Total Profit: ${totalprofit}",f"Average Change: ${avgchng}",f"Greatest Increase in Profits: {mxdate} (${maxdiff})",f"Greatest Decrease in Profits: {mindate} (${mndiff})"]


with open("budget_main.txt", "w") as text_file:
    for i in line:
        print(i)
        print(i, file = text_file)

os.startfile(txtpath)


