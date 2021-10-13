
# Problem:
# https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/practice-problems/algorithm/gift-for-almas-3-33d2f7c7/

# On his birthday, Almas was given a nxn(1<=n<=500) matrix of natural numbers up to 500 and instructions for it. 
# The instruction consisted of symbols L and R, where if the symbol L is given you need to rotate the matrix  90 degrees to the left, 
# and for the symbol R you need to rotate the matrix 90 degrees to the right. The instruction was only 3 characters in length so Almas could handle the twists with ease. 
# Your task is to display the matrix that Almas had at the end of these turns.

# Input

# The first line consists of one integer  n- the size of the matrix.

# In the next n lines, you are given n integers. Numbers can range 1 from  to 500.

# Output

# Output the final matrix nxn.

# Note

# Important note - you should not print any whitespace or newline if it is not necessary

# Sample Input:
# 2
# 1 2
# 3 4
# RLR

# Sample Output:
# 3 1
# 4 2


import numpy as np
# Write your code here
#define matrix
matrix=[]
Rnum=0
Lnum=0
#take input
n=int(input("\n"))
#print(n+2)

#print("Enter matrix values ")
#take input for each row
a=[] #declaration
for i in range(n):
    #print("Enter a row")
    a=list(map(int, input().split()))
    matrix.append(a)

#rotation  matrix 
#unable to write for n dimensions
# for Right rotate 90 degrees, last row->first column, so . on, till first row -> 
#last column
# for Left rotate 90 degrees, its opposite.
# last column-> first row, so. on till first column-> last row. 
mat=np.array(matrix)  # converting all matrices into numpy arrays for ease of computations
#mat[1,:]
Rmat=np.array([[0]*n]*n) # intialise
#Rotation  matrix 
#unable to write for n dimensions
# for Right rotate 90 degrees, last row->first column, so . on, till first row -> last column
# for Left rotate 90 degrees, its opposite.
# last column-> first row, so. on till first column-> last row.
'''def Rshift():
  for i in range(n): 
    Rmat[:,i]=mat[n-1-i,:]
  return Rmat

  Lmat=np.array([[0]*n]*n)  #intialise
def Lshift():
  for i in range(n):
    Lmat[i,:]=mat[:,n-1-i]
  return Lmat
'''
# when I use Rshift(matrix), I am getting error

#RSHIFT
def Rshift():#finding columns of result
  
  for i in range(n): 
    a[i]=mat[n-1-i] # a has all rows  of mat; last to first
  #print(a)
  #print(type(a)) 
  for j in range(n):
    Rmat[:,j]=a[j]
  return  Rmat

#LSHIFT
Lmat=np.array([[0]*n]*n)  #intialise
def Lshift():#finding rows of result  
  for i in range(n): 
    a[i]=mat[:,n-1-i]   # a has all colums of mat, last to first
  #print(a)
  #print(type(a)) 
  for j in range(n):
    Rmat[j]=a[j]
  return  Rmat
#ROTATION
rot_command=input()
for letter in rot_command:
  if letter == 'R':
    #Rnum ++
    Rnum=Rnum+1
    mat=np.copy(Rshift())
    
 ##   print("matrix after",Rnum,"th R shift is", mat )
  elif letter == 'L':
    Lnum=Lnum+1
    mat=np.copy(Lshift())
 #   print("matrix after",Lnum,"th L shift is", mat )
  else:
    print("Invalid Rotation Command")

#print matrix
for i in range(n):
    for j in range(n):
        print(mat[i][j], end=" ")
    print()
