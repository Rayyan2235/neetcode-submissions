# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([(root, float("-inf"), float("inf"))])
        
        while q:
            node, left, right = q.popleft() #ex1: 2, -inf, inf
            if not (left < node.val < right):
                return False
            if node.left:
                q.append((node.left, left, node.val))
            if node.right:
                q.append((node.right, node.val, right)) # this is how its supposed to be set up so that when we compare using the if statment, if lst is < than root which is < rst then true
    # Also note, double brackets because we are appending the above as one tuple


        return True

        

        '''
        init the q(root, -inf)
        while q
            popleft and store the root value (2)

            if left node and right node present:
                if left node < root val and right node > root val
                    return true

            if Left node is present:
                    check if node.left < stored root val
            if right node 
                    check if node.right > stored root val

            

        '''
        