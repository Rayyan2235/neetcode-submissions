'''
GOAL:
Pattern: String Manipulation
Key Technique: Using "#" as a delimeter, string splicing using 2 pointers
Logic:
Decode Function:
Loop through encoded string:

Find the length by scanning digits until #

Use that length to grab the next word

Append to result

'''



class Solution:
    #["neet","code"] -->"4#neet5#co$de"
    def encode(self, strs: List[str]) -> str:
        res =""
        for i in strs:
            res += str(len(i)) +'#' + i       
        return res     

    #"4#neet5#co$de" --> ["neet","code"]
    def decode(self, s: str) -> List[str]:
        res = []
        i= 0
    # now we want to iterate over the string, and only take the n chars after the # 
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1: j+1+length])
            i = length + j + 1
        return res





