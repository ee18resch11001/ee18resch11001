# https://leetcode.com/problems/happy-number/
# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

def checknumber(a=0):
    num = input("Enter number\n")
    num = int(num)
    if 232>num >= 0:
        print("check passed\n number is valid")
        num=int(num)
        timer=0
        while True:
            u=num%10
            h = num//100
            t = num//10-h*10
            num1=u*u+t*t+h*h
            if num1==num:
                print("number doesnot change after updation")
                break
            num=num1
            print("the digits for current number are",h,t,u)
            print("updated number is",num)
            
        
            timer=timer +1
            if timer==100:
                break
        if(num==1):
            print("number is happy")
        else:
            print("number is not happy")
    else:
        print("invalid number")
    
checknumber()

