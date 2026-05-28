class Solution:
    def isValid(self, s: str) -> bool:
        '''
        We use Stack because we are trying to use LIFO to pop the last element therefore create a list

        we create a hashmap to indicate what matches the closing bracket

        #NOTE: There is never a closing bracket in the 'stack' list

        Problems I faced:
            Didnt know how to implement a stack.
            Also didnt know how to make it such that when we have an open bracket, how can we find the specific bracket so that we could pop:
                this is done by the hashmap as we assign a closing bracket to an open bracket such that if the open bracket is seen in the list
                -then we look at the values in the dict and it matches whats in i then it pops it
                else its false
        




        '''



        stack = [] # So we can eliminate the bracket that was last inserted

        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for i in s:
            if i in closeToOpen: # We are checking if the char is any type of closing bracket
                if stack and stack[-1] == closeToOpen[i]: #If there is a non empty list AND the last element (which must be any type of OPENING bracket) = the value pair of it (which must be a CLOSING bracket) will be popped
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i) # This only occurs when 'i' is any type of opening bracket
                
        
        return True if not stack else False







        