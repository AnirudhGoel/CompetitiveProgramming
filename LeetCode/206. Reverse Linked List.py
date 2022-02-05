206. Reverse Linked List

# Iterative Approach
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        first = head
        second = first.next
        first.next = None
        
        while second is not None:
            temp = second.next
            second.next = first
            first = second
            second = temp
        
        return(first)

# Simple Recursive Approach
class Solution:
    def flipMapping(self, curr, nex):
        if nex.next:
            self.flipMapping(curr.next, nex.next)
        else:
            # this means we are at the last node, which will be the new head
            self.new_head = nex
        
        nex.next = curr
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        self.new_head = None
        
        self.flipMapping(head, head.next)
        
        # for first node
        head.next = None
        
        return(self.new_head)