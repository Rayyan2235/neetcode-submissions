# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        dist = 0
        stack = [[root, 1]]
        
        while stack:
            #Stack begins with the first element and depth of 1
            node, depth = stack.pop() # pops those elements and looks for children


            if node:
                dist = max(dist, depth) # First arg is itself, 2nd is whats being updated
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return dist

'''
            Mistakes:
             stack = [[root], 1]. I did this, which created a list of 2 elements rather than a list with 2 columns
             return dist was out of the loop thats why the max return value was 1.



            '''
                

