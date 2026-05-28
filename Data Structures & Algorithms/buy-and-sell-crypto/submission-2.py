class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        '''
        DP Problem

We keep updating profit with the previous days profit we keep updating minBuy to the next days minBuy
 if its smaller so that we can find the smallest buy day and pair it with the largest sell day
        '''
        profit = 0
        minBuy = prices[0]

        for i in prices:

            profit = max(profit, i - minBuy)
            #We update minBuy with the info we have
            minBuy = min(minBuy, i)  #minBuy moves to the next day if its less
        return profit





