# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None: 
            return l1
        if l1.val < l2.val: # determine which has the smaller head
            l1.next = self.mergeTwoLists(l1.next, l2) # recursively set the head value to the head of the next merged result
            return l1 
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

