# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        cnt = 0

        def dfs(root):

            nonlocal cnt

            if not root:
                return 0

            left = dfs(root.left) #Traverses through the tree using these
            right = dfs(root.right)
            cnt = max(cnt, left + right) # Only called at the end nodes, and works upwards

            return 1 + max(left, right) #  this calculates the height of the root, for instance at node 1, it checks if node 1 has a left child
            #so it runs 'dfs' with a 'None' arg, then 
        dfs(root)
        return cnt
        