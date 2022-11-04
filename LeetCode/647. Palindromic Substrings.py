# 647. Palindromic Substrings

# Solution: 90% faster in first attempt, yay!
class Solution:
    def calcPalin(self, s, l, r):
        count = 0
        
        while 0 <= l <= r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            count += 1
        
        return count
    
    def countSubstrings(self, s: str) -> int:
        num_palin = 0
        for i in range(len(s)):
            num_palin += self.calcPalin(s, i, i)
            num_palin += self.calcPalin(s, i, i+1)
        
        return num_palin