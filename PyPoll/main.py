import os
import pandas as pd

csvpath = r"C:\Users\bastaw1\PycharmProjects\GitHub\Python-Challenge\PyPoll\election_data.csv"

df = pd.read_csv(csvpath)

totalvote = len(df['County'])

CanName = df['Candidate'].value_counts().index.tolist()
CanCount = df['Candidate'].value_counts().values.tolist()
Canpct = [round(i / totalvote * 100, 2) for i in CanCount]

columns = ['Name', 'Votes', 'Percentage']
df1 = pd.DataFrame(columns = columns)
df1['Name'] = pd.Series(CanName)
df1['Votes'] = pd.Series(CanCount)
df1['Percentage'] = pd.Series(Canpct)
max = df1['Percentage'].max()
winner = df1.loc[df1['Percentage'] == df1['Percentage'].max(), 'Name'].tolist()
sep = "---" * 15


def candidates():

    for i in range(0, len(df1)):
        print(f"{df1['Name'][i]}: {df1['Percentage'][i]}% ({df1['Votes'][i]})")
        print(f"{df1['Name'][i]}: {df1['Percentage'][i]}% ({df1['Votes'][i]})", file = text_file)


list1 = [f"\nElection Results", sep, f"Total Votes: {totalvote}", sep]
list2 = [sep, f"Winner: {winner[0]}", sep]

with open("PyPoll_main.txt", "w") as text_file:
    for i in range(len(list1)):
        print(list1[i])
        print(list1[i], file = text_file)
    candidates()
    for x in range(len(list2)):
        print(list2[x])
        print(list2[x], file = text_file)

os.startfile("PyPoll_main.txt")