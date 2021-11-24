import numpy as np

# Funtion for printing my details
def print_details():
    details = {"Assignment Name": ': Matrix ',"Date": ': 01 NOV 2021',"Time Taken":" : 5 hours","Reference1":': https://www.kite.com/',"Reference2":': https://www.w3schools.com/',"Reference3":': https://numpy.org/doc/stable/user/basics.html',"Reference4":': https://stackoverflow.com/',"Author name":': B Madhan',
    "Take away":': Learnt about numpy module and list operations'}
    for key, value in details.items():
        print("{:<10} {:<10}".format(key,value))
        print(" ")
    print(" ")

# Function for getting the matrix
def getting_matrix():
  print("Enter the matrix and number of task :")

# n = row,column size, k = number of task
  n,k=input().split()
  n,k=[int(n),int(k)]
  matrix=np.zeros((n,n), dtype=int)
  print("Initial Matrix :")
  print(matrix)
  print(" ")
  perform_task(matrix,n,k)

# Function for performing the tasks
def perform_task(matrix,n,k):
  ans=[]
  for a in range(k):
    print("Enter row and column no for task:",a+1)

# i = row value for the task, j = column value for the task 
    i,j=input().split()
    i,j=[int(i),int(j)]
    i=i-1
    j=j-1
    count=0
    index=[]
    for row in range(n):
      for column in range(n):
        if row==i or column==j:
           matrix[row][column]=1
        if matrix[row][column]!=1:
          # count = number of empty cells in the matrix
          count=count+1
          index.append([row,column])
          index1=map(str,index)
    print(matrix)
    print(list(index1),"Count:",count)
    print(" ")
    
    # ans = appending and printing the count of all tasks
    ans.append(count)
    ans1=map(str,ans)
  print("Ans:",list(ans1))

# Calling functions
print_details()
getting_matrix()