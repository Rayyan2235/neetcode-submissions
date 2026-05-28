class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            Brute force
            Iterate 2 times
            
        PROBLEMS:
        First error:  profit = sell[prices] - buy[prices]
             ~~~~^^^^^^^^
TypeError: 'int' object is not subscriptable
        A) I accidentally the integer outside the square brackets thinking that accesses the array, but its the other way round

2nd) Wasnt sure why we didnt start with buy and sell to be first and last element
and using the while statement like it is
A) each element (their index) represents the day to be bought or sold. Therefore, if we do the traditonal way, we shouldnt back in time 
prices[l] < prices[r] → false (7 > 4)
So we move one pointer — but which one? 🤔

If you move r left, you’re checking an earlier sell day.
If you move l right, you’re checking a later buy day.

        '''
        buy = 0 
        sell = 1
        res = 0
        
        

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                res = max(res, profit)

            else:
                buy = sell

            sell += 1
        return res


