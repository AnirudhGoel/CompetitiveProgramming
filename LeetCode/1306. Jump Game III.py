# 1306. Jump Game III

# Solution 1: Standard BFS

from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        q = deque()
        
        q.append(start)
        visited.add(start)
        
        while q:
            i = q.popleft()
            
            if arr[i] == 0:
                return True
            
            if i + arr[i] < len(arr) and i + arr[i] not in visited:
                q.append(i+arr[i])
                visited.add(i+arr[i])
            
            if i - arr[i] >= 0 and i - arr[i] not in visited:
                q.append(i-arr[i])
                visited.add(i-arr[i])
        
        return False