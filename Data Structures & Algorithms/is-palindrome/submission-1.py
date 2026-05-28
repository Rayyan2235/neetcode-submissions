class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Palindrome means that the sentence or word is the same front and back
        #So if we reverse the string, it should come out the same if it is a plaindrom

        new = ""
        for i in s: #iterating rhough each individual char
            if i.isalnum():  # This jus checks if it contains alphanumerics. This means we arent taking special chars like 'space' 
                new += i.lower()
        return new == new[::-1] # checks if original string is the same as reverse string


        