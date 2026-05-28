class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        h = # of hours I have to eat 
        piles[i] = number of bananas in that index
        find the smallest k number of banaanas/hour eaten.     

        How to access the final index of the array   

        '''

        l = 1  # Initially thought should equal 0 but realized k cant b 0 
        r = max(piles) # Used to get the max value in piles
        res = r # want the k value to start from the top since we are finding min value of k

        while l <= r:     
            k = (l + r) // 2   
            hours = 0

            for pile in piles:
                hours += math.ceil(pile/k) # Formula to count how many hours its gonna take to eat k times an hour for that specific pile

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res

                


            

        