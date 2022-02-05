# 142. Linked List Cycle II

# Cleaner code
class Solution:
    def meetingPoint(self, n1, n2):
        while n1 != n2:
            n1 = n1.next
            n2 = n2.next
        return n1
    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        t = head.next
        h = head.next.next
        
        while h and h.next:
            if t == h:
                return self.meetingPoint(t, head)
            t = t.next
            h = h.next.next
        
        return None

# Faster (for leetcode) version
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        t = head.next
        h = head.next.next
        
        while h and h.next:
            if t == h:
                while t != head:
                    t = t.next
                    head = head.next
                return t

            t = t.next
            h = h.next.next
        
        return None