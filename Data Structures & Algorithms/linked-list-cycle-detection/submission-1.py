# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        How do we know if a LL is a cycle?
            1) If the tail nodes.next != None
        '''
        curr = head
        visited = set()

        while curr:
            if curr in visited:
                return True
            visited.add(curr) # We add the whole node 
            curr = curr.next
        return False
            

        