# 430. Flatten a Multilevel Doubly Linked List

# Iterative simple approach
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        stack = list()
        
        while curr or stack:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                curr.next = curr.child
                curr.next.prev = curr
                curr.child = None
            
            if not curr.next and stack:
                curr.next = stack.pop()
                curr.next.prev = curr
            
            curr = curr.next
        
        return head

