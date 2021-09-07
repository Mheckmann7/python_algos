# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr != None:
            nextTemp = curr.next # must store reference to next element
            curr.next = prev # reverse the pointer  
            prev = curr # set the next iteration 
            curr = nextTemp # move to next node
        return prev
        