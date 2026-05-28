class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        k:v -> 

        '''
        
        ls = [[] for i in range(len(nums) + 1)]
        count ={}

        for i in nums:
            count[i] = 1 + count.get(i, 0) # Updates the k:v to number : times its repeated

        #Now that we updated the dictionary with the numeber: times its repeated. Lets append it to the lists
        for num, index in count.items():
            #Since we want to add the number to the list. And the index of the list reps the repition of the num
            ls[index].append(num)

        res = [] # we need to retunit as a list
        #Now we want to assign the empty [] where index reps the number of times

        for j in range(len(ls) - 1, 0, -1):
            for l in ls[j]:
                res.append(l)
                if len(res) == k:
                    return res











        