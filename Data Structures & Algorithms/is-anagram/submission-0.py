class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if the lengths of both strings are equal
        if len(s) != len(t):
            return False
        
        # Sort the characters in both strings
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        
        # Compare the sorted strings
        return sorted_s == sorted_t
