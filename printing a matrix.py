# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 14:04:20 2021

@author: Subhash
"""
# question:A basic code for printing matrix , taking elements input from user 
#     take inputs from user given by format
#     1)number of rows
#     2)number of columns
#     3)elements one by one , press enter after each integer input
#     Expected output in matrix format
#     Run the code to check yourself the formats


  
R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
  
# Initialize matrix 
matrix = [] 
print("Enter the entries rowwise:one element at a time followed by enter") 
  
# For user input 
for i in range(R):          # A for loop for row entries 
    a =[] 
    for j in range(C):      # A for loop for column entries 
         a.append(int(input())) 
    matrix.append(a) 
  
# For printing the matrix 
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print() 
    
