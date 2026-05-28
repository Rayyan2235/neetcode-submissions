class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


#key : value --> ('a', 'e', 't') : ['eat', "tea"...] 
#The key is a tuple because its immutable and cannot be changed as opposed to a list
        res = defaultdict(list)

        for i in strs:
            count = [0] * 26

            for c in i:
                count[ord(c) - ord('a')] += 1 #Add a 1 on the index of the 'c' element
#After iterating throug all words in the list and the specifc letters in each lsit
           
            res[tuple(count)].append(i) # key is the index of the letters that are 1 which reps the letters in a tuple
            # , and we append the word as the value

        return list(res.values())



        