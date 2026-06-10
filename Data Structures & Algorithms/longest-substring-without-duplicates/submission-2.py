class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        maxS = 0
        

        for r in range(len(s)):
            while s[r] in seen: # We use While instead of if to remove multiple from seen hashset at a time if need be. Look at CASE 3
                seen.remove(s[l])
                l += 1
            seen.add(s[r])     

            maxS = max(maxS, r - l + 1)
            
        return maxS




        