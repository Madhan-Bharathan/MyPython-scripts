# Importing the required modules
import os
from termcolor import colored

# Function to print the details
def print_details():
    details = {"Assignment Name": ': Shuffling or Scrambling ',"Date": ': 04 NOV 2021',"Time Taken":" : 15 hours","Reference1":': https://pypi.org/project/termcolor/',"Reference2":': https://www.w3schools.com/',"Reference3":': https://www.geeksforgeeks.org/',"Reference4":': https://stackoverflow.com/',"Author name":': B Madhan',
    "Take away":': Great learning about string operations, various ways of using list and coloring in python'}
    for key, value in details.items():
        print("{:<10} {:<10}".format(key,value))
        print(" ")
    print(" ")

# Function for getting the input
def gettingInput():
  punct = (".", ";", "!", "?", ",")
  # Defining the required variables
  new_word = ""
  result = ""
  new_list = []

  # Getting the inputs
  inputfile = input("Enter input file name (text.txt): ")
  file_path='text.txt'

  # Checking if the file is empty
  if os.stat(file_path).st_size == 0:
    print('File is empty')
  else:
    numberOfRun=int(input("How many times you want to shuffle:"))
    for j in range(0,numberOfRun):
      # Reading the file
      with open(inputfile, 'r') as fin:
        # Read line by line in txt file
        for line in fin.readlines():  
          # Read word by word in each line
          for word in line.split():

            # Calling the Shuffling function
            new_word=shuffling(word,punct,j,new_word)
      for l in new_word.split():

        # Calling the colouring function
        new=coloring(l)
        new_list.append(new)
      result = result + ''.join(new_list) + " "
      print("Try:",j+1)

      # Printing the result
      print(result)

      # Resetting the variables
      new_word = " "
      result = " "
      new_list = []

      
# Function for shuffling the words
def shuffling(word,punct,j,new_word):
  # Making sure If word length > 3
  if len(word) > 3:  

    # Checking if the word ends with punctuation
    if word.endswith(punct):
      word1 = word[1:-2]

      # Shuffling even characters
      if j%2==0:
        i=0
      # Shuffling odd characters
      else:
        i=1
      list1=[]
      list1[:0]=word1
      while i<len(word1) and i+2<len(word1):
        temp=list1[i]
        list1[i]=list1[i+2]
        list1[i+2]=temp
        i=i+4
      list1.insert(0, word[0])
      list1.append(word[-2])
      list1.append(word[-1])
    else:
      word1= word[1:-1]
      # Shuffling even characters
      if j%2==0:
        i=0
      else:
      # Shuffling the odd characters
        i=1
      list1=[]
      list1[:0]=word1
      while i<len(word1) and i+2<len(word1):
        temp=list1[i]
        list1[i]=list1[i+2]
        list1[i+2]=temp
        i=i+4
      list1.insert(0, word[0])
      list1.append(word[-1])
    new_word = new_word + ''.join(list1) + " "
  # If the word length < 3 directly append the word
  else:
    new_word = new_word + word + " "
  return new_word

# Function for colouring the letters respectively
def coloring(new_word):
  word=""
  length=len(new_word)
  li=[]
  li[:0]=new_word
  for chars in range(0, len(li),1):
    if chars<=length-1:

      # Colouring the first characters
      if chars==0:
        temp=colored(new_word[chars], 'yellow')
        li[chars]=temp
      # Colouring the last characters
      elif chars==length-1:
        temp=colored(new_word[chars], 'yellow')
        li[chars]=temp
      # Colouring the even characters
      elif chars%2==0:
        temp=colored(new_word[chars], 'red')
        li[chars]=temp
      else:
      # Colouring the odd characters
        temp=colored(new_word[chars], 'blue')
        li[chars]=temp
  new_word=""
  new_word = new_word + ''.join(li) + " "
  new_word = new_word + word
  # Returning the coloured words
  return new_word
  
# Calling the functions
print_details()
gettingInput()