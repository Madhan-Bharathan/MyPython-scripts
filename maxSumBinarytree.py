from binarytree import tree

class bit:

# Funtion for printing my details
  def print_details():
      details = {"Assignment Name": ': Greedy Approach or Technique to find the maximum sum and its path in binary tree',"Date": ': 28 OCT 2021',"Time Taken":" : 9 hours","Reference1":': https://replit.com/@GaneshManoharan/NonGreedyApproachBinTree#main.py',"Reference2":': https://www.geeksforgeeks.org/binarytree-module-in-python/',"Reference3":': https://www.techiedelight.com/find-maximum-sum-root-to-leaf-path-binary-tree/',"Reference4":': https://stackoverflow.com/',"Author name":': B Madhan',
      "Take away":': In depth understanding and the ways of traversing in binary tree, Learnt the binary tree modules in python'}
      for key, value in details.items():
          print("{:<10} {:<10}".format(key,value))
          print(" ")
      print(" ")
  
# Funtion for printing the tree, maximum sum
  def print_tree():
    try:
      # Getting binary tree level from user
      l=int(input("Enter the level of binary tree b/w 1-9:"))
      # Enter 1 for perfect tree or 0 for imperfect tree
      p=int(input("Perfect=1,imperfect=0:"))
      bit.print_tree(l,p)
      n=tree(l,is_perfect=p)
      print(n)
      s=bit.max_sum(n)
      print("The maximum sum is:",s)
      print("The maximum sum path is :", end=' ')
      bit.path(n, s)
    except:
      print("Either level of binary tree is not 0-9 or perfect/imperfect is other than 0 or 1")

# Funtion to calculate the maximum sum
  def max_sum(root):
      if root is None:
          return 0
      left = bit.max_sum(root.left)
      right = bit.max_sum(root.right)
      return (left if left > right else right) + root.values[0] 

# Funtion to find the path which gives the maximum sum
  def path(n,s):
    if s == 0:
      return True
    if n is None:
      return False
    left = bit.path(n.left, s - n.values[0])
    right = bit.path(n.right, s - n.values[0])
    if left or right:
        print(n.values[0], end='<-') 
    return left or right
    
# Calling the functions
bit.print_details()
bit.print_tree()