# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        begin = ListNode()
        l3 = begin
        
        while(l1 or l2):
            if l1 is None:
                l1 = ListNode()
                
            if l2 is None:
                l2 = ListNode()
            
            total = l1.val + l2.val + carry
            
            l3.val = int(total % 10)
            carry = int(total / 10)
            
            l1 = l1.next
            l2 = l2.next
            
            if l1 or l2 or carry == 1:
                l3.next = ListNode()
                l3 = l3.next
            
        if carry == 1:
            l3.val = 1
            l3.next = None
            
        return begin