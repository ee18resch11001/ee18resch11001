# https://leetcode.com/problems/generate-parentheses/
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8





class Solution
    def generateParenthesis(self, n int) - List[str]#whats happening here
        results=[]
        #
        
        #use recursion
        def generaterecursively(results,currentresult,openbraces,closedbraces)
            #print(test1)
            
            if openbraces==0 and closedbraces==0
                
                results.append(currentresult)
              #  print(results)
            #currentresult is the final result
                #add that to the list results
                return
          
            if openbracesclosedbraces
                 return
          
            if openbraces0 or closedbraces0 
                 return
          
            if openbraces=closedbraces
              #  print(test)
            
         
          #normal case
          #how do I add a string to list
          #ans. for example to add string element a=apple, do results.append(a) 
          #add char to string

        #   '''def addopenbrace(currentresult)
         #   a=currentresult
        #    a=a+'{'
         #   return a
         #   openbraces-=1
         #   '''
                #add openbracket
                generaterecursively(results,currentresult+'(',openbraces-1,closedbraces)

                #add closedbracket
                generaterecursively(results,currentresult+')',openbraces,closedbraces-1)
                return results
        return generaterecursively([],,n,n)        
        
#problem results , I have not returned before, so it was local variable.
#in case of sir's code, he used non primitive variavle list of str in java, so it called by reference.
#ask sir, when function calls by value and when by reference
#next time, record the solving function in obs.


          


        #it should return same function generate(results, openbraces-1,closedbraces-1)