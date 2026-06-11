class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Hashmap keeps track of how many of each letter is present

        then we have a formula: window_len - max_freq (of the letter) <= k
            then update our max_substring
        else
            we shrink from left hand side
        '''


        l = 0
        substr = 0
        hm = {}
        maxF = 0
        winL = 0

        '''for m in range(len(s)):
            s[m] = 1 + hm.get(s[m], 0)
        # {A: 4, B: 3} Therefore, maxFreq = 4'''

        for r in range(len(s)):
            hm[s[r]] = 1 + hm.get(s[r], 0)
            
            maxF = max(hm.values())
            winL = (r - l) + 1
            
            if winL - maxF <= k:
                substr = max(substr, winL)
                
            else:
                hm[s[l]] -= 1
                l+= 1

            
        return substr
            



        