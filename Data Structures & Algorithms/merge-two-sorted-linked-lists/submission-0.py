# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dum = ListNode() # we need this dummy node because we are creating a NEW list from l1 aand l2
        #Why? Because to add anyth toa linkedlist we need a head, so if tehres no head then we cant simply compare and add it to a list. We create this dummy node to pretend like a linkedlist alr exists, so we can build on top of that
        tail = dum

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next # want to keep incrementing regardless of the condition

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        

        return dum.next # dum points to the head of the linkedlist therefore returning the whole list as opposed to tails. Dum and tails are both pointers that initially point towards the empty list node
        