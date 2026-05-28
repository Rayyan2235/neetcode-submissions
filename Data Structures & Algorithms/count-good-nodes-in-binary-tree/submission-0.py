# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque()

        q.append((root, -float('inf'))) # Holds a tuple with 2 elements. Initially, (2,-inf), then maxval gets updated to a value
        # reason init is -inf is because the root node always has to be a good node, the tree can contain negative numbers too so using a 0 is not possible either

        while q:
            node, maxval = q.popleft() # Popping (2,-inf) tgt
            if node.val >= maxval:
                res+= 1
            
            if node.left:
                q.append((node.left, max(maxval, node.val))) # append the left node andor the prev maxval or the current nodeval

            if node.right:
                q.append((node.right, max(maxval, node.val)))

        return res

             

        