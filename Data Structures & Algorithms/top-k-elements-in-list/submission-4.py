class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        GOAL: Find Top K Freq Ele
        PATTERN: Bucket Sort, using {} since it asks for 'frequency'
        LOGIC: Using a [] to represent the number of times a number has been repeated
        - we then iterate backwards to get the most frq ele because those would have larger index as the index
        is determined by the number of times its repeated
        
        MISTAKES: 
        '''



        count= {}
        freq = [[] for i in range(len(nums)+ 1)]

        #index of [] reps the number of times repeated i.e 2x = index 2

        for i in nums:
            count[i] = 1 + count.get(i, 0)# key : value --> the number : times its repeated 
            #Now we want to assign the empty [] where index reps the number of times
        for num, cnt in count.items():
            freq[cnt].append(num) # if cnt = 2, then freq[cnt] is accessing the 2nd [] and appending num

        res = []
        #Over here we are trying to append the most freq (the last k freq) into res


        #Now we iterating through the freq backwards to get the top most freq and appending it into res to return as a list 
        for i in range(len(freq)- 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res


        

        