# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [] # to create the outer list

        q = collections.deque() #init a Q
        q.append(root) # add the root

        while q:
            qlen = len(q)
            lvl = [] # The innter list for each level
            for i in range(qlen):
                node = q.popleft()
                if node:
                    lvl.append(node.val) 
                    #BFS logic:
                    q.append(node.left)
                    q.append(node.right)
            if lvl:
                res.append(lvl)
        return res


        '''
        Init mistake was 'level.append(node)' without the .val, this just provided me with the reference of node.
        '''


        