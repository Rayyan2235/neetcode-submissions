class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ls = [[] for i in range(len(nums) + 1)]
        count = {}

        for i in nums:
            count[i] =1 +  count.get(i, 0) #Looks up key i in the dictionary count.
#If the key exists, it returns the value for that key.

        for num, cnt in count.items():
            ls[cnt].append(num) # Rem we are adding this to a list
        
        res = []

        for i in range(len(ls) - 1, 0, -1):
            for j in ls[i]:  # This checks the value of the key ls[i]
                res.append(j) 
                if len(res) == k:
                    return res
"""
      We need to first create a bucket sort nums number of lists
      create a dictionary to initially store kv pairs as number: repititon

      The list will be arranged in order of index, so highest count = highest index list
      therefore, iterate over count.items() to get access to the key (so we can access the specific indexed list)
      and access to the values to get the number thats been repeated

      then we iterate through the lists backwards cuz the numbers repeated the most will be at the top

"""
    








        