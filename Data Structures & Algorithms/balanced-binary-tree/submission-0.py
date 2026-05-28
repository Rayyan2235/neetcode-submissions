# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            
            check_balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1 # the reason its less than one is because if it is greater than it indicates that it is an incomplete binary tree whichh is unbalanced since if there is greater than 1 then it means there are 2>= nodes
            return [check_balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

        



        