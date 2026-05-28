# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        '''
        Linked List = nodes = data, address
        We have 2 pointers one on the current node and the other one behind (prev node)
        once we traverse through the linked list we set the next node to the prev


        '''
        prev = None
        curr = head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp # We set it to the tmp because thats the bridge we burnt and for every link we break we tie it back to that 
        return prev

'''
    Concept I had difficulty understanding was curr.next whether it the value points to the next node.
    I thought curr.next just points to the next node but realized that it is more intricate thant that
    curr.next refers to the 2nd field in a node (val, next(reference of next node)) so while it does read the val of the next node
    it is still withing the same node so if we overwrite it, it will adjust the curr nodes direction


'''


     

        