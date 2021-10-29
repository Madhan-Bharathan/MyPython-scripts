# Importing necessary modules for the program
import re
import colorama
from colorama import Fore, Style
import time
import pandas as pd

# Printing my details
details = {"Name": 'B Madhan',"Date": '8 OCT 2021',"Time Taken":"9 hours","Reference1":'https://www.geeksforgeeks.org/',"Reference2":'https://stackoverflow.com/',
"Reference3":'https://www.w3schools.com/'}

for key, value in details.items():
    print("{:<10} {:<10}".format(key,value))
    
# Function 1 - Printing the letters randomly
def random_number(n): 
  digit = int(str(time.time()).split('.')[-1][-1]) 
  if digit <= len(n) : 
    return n[digit-1] 
  else: 
    new_digit = digit-len(n) 
    return n[new_digit] 

# Writing the output to a file
with open("test.txt", "w") as external_file:
  print(*(random_number(['A','T','G','C','N']) for _ in range(2048)),sep="", file=external_file)
  external_file.close()

print("\n Function 1 \n Printing the contents of the file generated\n")
print(*(random_number(['A','T','G','C','N']) for _ in range(2048)),sep="")

f = open("test.txt",'r').read()
n = 32

# Function 2 - Calculating the number of occurrences and Percentage
def calculation(str):
  tot=len(str)
  a=str.count("A")
  t=str.count("T")
  g=str.count("G")
  c=str.count("C")
  n=str.count("N")
  at=str.count("AT")
  gc=str.count("GC")
  aper=(a/tot)*100
  tper=(t/tot)*100
  gper=(g/tot)*100
  cper=(c/tot)*100
  nper=(n/tot)*100
  atper=(at/tot)*100
  gcper=(gc/tot)*100

  # Printing the data in table format
  df=pd.DataFrame({"Total Bases":['A','T','G','C','N','AT','GC'],
                 "2048":[a,t,g,c,n,at,gc],"PERCENTAGE":[aper,tper,gper,cper,nper,atper,gcper]})

  print("\n Function 2 \n Printing the number of occurences of the characters and their Percentage\n")
  print(df)
  

# Function 3 - Identifying the Patterns
def sliding(f, n):
  splitted = [f[i:i+n] for i in range(0, len(f), n)]
  for line in splitted:
    res = re.sub(r'(ATTAAA)', Fore.LIGHTYELLOW_EX + r'\1' + Fore.RESET, line)
    res2 = re.sub(r'(CAT)', Fore.RED + r'\1' + Fore.RESET, res)
    res3 = re.sub(r'(TATA)', Fore.CYAN + r'\1' + Fore.RESET, res2)
    res4 = re.sub(r'(AATAAA)', Fore.LIGHTRED_EX + r'\1' + Fore.RESET, res3)
    res5 = re.sub(r'(ATAGTCGC)', Fore.LIGHTCYAN_EX + r'\1' + Fore.RESET, res4)
    print(res5)

# Calling the functions
calculation(f)
print("\n Function 3 \n Identifying the Pattern occurrences and highlighting them with different colours\n")
sliding(f,n)