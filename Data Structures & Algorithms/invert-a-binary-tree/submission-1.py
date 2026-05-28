# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        root.left, root.right = root.right, root.left
        #Mistake made was that I overwrote root.right with root.left, this happens when you write the above code one line udenreachother

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        

        