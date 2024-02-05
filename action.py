import csv  
import pandas as pd

def function():
 username = ""
 FileName = ""
 username1 = ""
 Name = ""
 ReadFile = ""
 Filter = ""
 Whole = ""
 Choose = ""
 while username != "Exit":
  print("What to do?")
  username = input("Choose Option:")
  
  if username == "Create":
   FileName = input("Enter FileName:")
   f = open(FileName+".csv", "x")
   continue
  elif username == "Write":
   Name = input("Enter FileName:")
   with open(Name+'.csv', 'w', newline='') as file:
    header = input("Enter Headers:")
    text = input("Enter Text:")
    writer = csv.writer(file,delimiter=' ', quoting=csv.QUOTE_NONE, escapechar=',')
    writer.writerow([header])
    writer.writerow([text])
    print(header)
   continue  
  elif username == "Read":
   while ReadFile != "Back":
    ReadFile = input("Choose a File:")
    print('---------------------------')
    print("Choose Option To Read File")
    print('---------------------------')
    Filter = print("1. Filter:")
    Whole = print("2. Whole:")
    print('---------------------------')
    while Choose != "Back":
     Choose = input("Choose Option:")
     if Choose == "Filter":
      print('---------------------------')
      ColumeName = input("Enter Colume Name:")
      RowName = input("Enter Row Name:")
      print("--------------------")
      df = pd.read_csv(ReadFile+'.csv', escapechar=' ')
      df.set_index(ColumeName, inplace=True)
      print(df.loc[[RowName]])
      continue
     elif Choose == "Whole":
      df = pd.read_csv(ReadFile+'.csv', escapechar=' ')
      print(df)
      continue
     elif Choose == "Back":
         print("\n")	 
     else:
      quit()	 
    continue	

function()