class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ''' 
        Arrange the list and set it to negative values such that the largest number becomes the smallest when it snegative
        Turn this into a minheap (Max Heap)
        Compare 1st and 2nd ele
        return abs value
        

        '''
        
        stones = [-s for s in stones] # Updates stones to have all the numebrs but just negative
        # waht this does is that the largest number will now become the smalles (6--> -6) therefore first to be popped

        heapq.heapify(stones)
        while len(stones) > 1:
                
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
           
            if first < second:
                heapq.heappush(stones, first - second) # takes 2 arg, 1) push to where, 2) what we pushing

        
        return abs(stones[0]) if stones else 0


        '''
        Mistakes I made:

        Line 18: I did first > second thinking first will always be greater as we are using a max heap appraoch,
         -however I forgot we dealing with negative numebers

        line 22 - We still have negative valeus and I forgot to return the abs value of the int



        '''
            





        
        
        