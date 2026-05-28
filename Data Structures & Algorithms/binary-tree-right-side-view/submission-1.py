# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        q = deque([root])


        while q:
            qLen = len(q)
            rhs = None
            for i in range(qLen):
                node = q.popleft()
                if node:
                    rhs = node
                    #BFS logic:
                    q.append(node.left)
                    q.append(node.right)
            if rhs:
                res.append(rhs.val)
        return res
'''
BFS logic:
1) Init Q
2) Init empty list to store vals
3)Outer loop and inner loop based on question
4)Find length of queue and iterates based on that because that is the main condition for our func to work
5)BFS logic appending node into queue
6) return res 


'''



        
    
       



        
        