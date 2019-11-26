import csv_reader
import clue_answer
from msvcrt import getch

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTWzgjSUGq5NtoM_pvDo9yH_B9kI3EA2StAAa6nwtvk68m1iS-15AeOqhvTS8BK34KRemkjhEnACaVD/pub?gid=0&single=true&output=csv"
data = csv_reader.online_csv(url)
for i in range(0, len(data)):
  if data[i]["Position"]=='':
    continue;
  #p1=clue_answer.ClueAnswer
  attempt=clue_answer.clue_ans(data[i]["Clue"],data[i]["Solution"])
  if attempt == 'C':
    choice =input("Press any key to move ahead;\nPress 'Q' to quit now\n")
    if choice.upper()=='Q':
      break
  else:
    break  
print("Press any key to exit...")
getch()