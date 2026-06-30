# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head # temp pointer
        prev = None

        while curr is not None:
            tmp = curr.next #tmp pointer so that we can use it in the end to traverse linked list
            curr.next = prev # Set the next pointer to the previous MA
            prev = curr #Update prev to the next node
            curr = tmp# Traversing linked List
        return prev
        