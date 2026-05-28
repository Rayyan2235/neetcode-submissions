# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) # Using recurison 
        else:
            return False


    '''
    p =[1,2,3]
    q=[1,2,3]

    if p 
    checks if p is present
    if p == q
    checks if they contain the same elements which is the T for the above
    however, 
    p =[1,2,3]
    q=[1,3,2]
    this would also return True thats why we also check for the indivudual values as well 


    '''
        