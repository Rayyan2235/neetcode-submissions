class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "$" + i
        return res
        # res = 5$Hello4$Wrld      

    def decode(self, s: str) -> List[str]:
        '''
            Read the 5, go 5 steps ahead of the delimeter
        '''

        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "$": # Iterate until you reach the delimeter
                j+= 1
            length = int(s[i:j]) #length = 5
            i = j + 1 # Point at delimeter
            j = i + length # point at end of word
            res.append(s[i:j]) # therefore get the whole word
            i=j
        return res

