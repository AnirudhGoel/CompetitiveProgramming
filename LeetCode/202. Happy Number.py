# 202. Happy Number

# Solution 1: Stupid question, read solution from Leetcode
class Solution:
    def nextNum(self, n):
        sum = 0
        while n > 0:
            sum += (n % 10) ** 2
            n = int(n / 10)
        return sum
        
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n not in seen and n != 1:
            seen.add(n)
            n = self.nextNum(n)
        
        return True if n == 1 else False