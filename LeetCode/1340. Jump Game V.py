# 1340. Jump Game V

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        mem = dict()
        
        for i in range(len(arr)):
            if i not in mem:
                self.calculateJumps(arr, d, mem, i)
        
        return max(mem.values())
        
    def calculateJumps(self, arr, d, mem, i):
        if i in mem:
            return mem[i]
        
        left_max = 0
        for j in range(i-1, i-d-1, -1):
            if 0 <= j < len(arr) and arr[j] < arr[i]:
                left_max = max(left_max, self.calculateJumps(arr, d, mem, j))
            else:
                break
        
        right_max = 0
        for j in range(i+1, i+d+1):
            if 0 <= j < len(arr) and arr[j] < arr[i]:
                right_max = max(right_max, self.calculateJumps(arr, d, mem, j))
            else:
                break
        
        mem[i] = max(left_max, right_max) + 1
        
        return mem[i]