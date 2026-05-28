from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
          # Step 1: Count frequencies
        count = Counter(nums)  # {num: frequency}

        # Step 2: Get top k frequent elements using a heap
        return heapq.nlargest(k, count.keys(), key=count.get)
        '''theres a list with numbers
        theres an integer 'k' that indicates top 'k' numbers repeated
        for instance, k =2 tehrefore, return the top 2 repeated numbers 

        we can create a hashmap w the key being the number 
        and the value being the number of times it has been repeated
        and return the key with the highest value using (max(nums, key=nums.get))'''

        '''dict1 ={}

        for i in range(len(nums)):
            dict1[nums[i]] = 1 + dict1.get(nums[i], 0)
        return list[max(dict1, key=dict1.get)]
'''


     
        