class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            Brute force
            Iterate 2 times
            

        '''
        result = 0

        for i in range(len(prices)):
            buy = prices[i]
            print(len(prices))


            for j in range(i + 1, len(prices)):
                sell = prices[j]

                
                result = max(result, sell - buy)

        return result
        