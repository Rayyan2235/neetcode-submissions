class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums): #checks if it exceeds therefore we will have the list, and then since we have exceeded we will move to the pop line
                res.append(subset.copy())
                return
            
            #Decision: If we append the number rather than ignoring (Left subtree)
            subset.append(nums[i])
            dfs(i + 1) # DFS logic

            #Decision: If we IGNORE the new numebr 
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

        '''
    What we are doing is manipulating the subset lists such that we can get different combinations
    -of the list nums

        '''


      
        