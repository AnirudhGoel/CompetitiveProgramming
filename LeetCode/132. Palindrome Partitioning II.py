# 132. Palindrome Partitioning II
# Note: From the Leetcode solutions, I thought of something similar to the solution 6 myself too. I was able to figure out the technique of scanning the string for palindromes by detecting patterns of palindrome (aa, aba) but then I wasn't sure how to select the partition with the least number of cuts

# Solution 1: Front Partitioning, implemented myself after reading watching this video for the approach - https://www.youtube.com/watch?v=_H8V5hJUGd0&ab_channel=takeUforward
# Works but faster than only 9%
class Solution:
    def partition(self, s, dp):
        if s in dp:
            return dp[s]
        
        if s == s[::-1]:
            return 0
        
        min_cuts = float('inf')
        
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1]:
                cuts = self.partition(s[i:], dp) + 1
                min_cuts = min(min_cuts, cuts)
        
        dp[s] = min_cuts
        return min_cuts
    
    def minCut(self, s: str) -> int:
        dp = dict()
        
        return self.partition(s, dp)

# Optimisation 1: Replace s[:i][::-1] with single expression (s[-len(s)+i-1:-len(s)-1:-1]) to get reverse slice
# 17% faster
class Solution:
    def partition(self, s, dp):
        if s in dp:
            return dp[s]

        if s == s[::-1]:
            return 0

        min_cuts = float('inf')

        for i in range(1, len(s)):
            if s[:i] == s[-len(s)+i-1:-len(s)-1:-1]:
                cuts = self.partition(s[i:], dp) + 1
                min_cuts = min(min_cuts, cuts)

        dp[s] = min_cuts
        return min_cuts

    def minCut(self, s: str) -> int:
        dp = dict()

        return self.partition(s, dp)

# Solution 2: Expanding around the center
# 93% faster, only trick is to handle case for l-1 going < 0
class Solution:
    def checkPalin(self, s, l, r, dp):
        while 0 <= l <= r < len(s) and s[l] == s[r]:
            if l == 0:
                prev_cut = -1
            else:
                prev_cut = dp[l-1]
            dp[r] = min(dp[r], prev_cut + 1)

            l -= 1
            r += 1


    def minCut(self, s: str) -> int:
        dp = [i for i in range(len(s))]

        for i in range(len(s)):
            self.checkPalin(s, i, i, dp)
            self.checkPalin(s, i, i+1, dp)

        return dp[-1]

# Alternate Solution 1:
# Just for practice (proves there's more than one way to solve a problem even with the same algo)
class Solution:
    def partition(self, s, mem):
        if s == s[::-1]:
            return 0

        if s in mem:
            return mem[s]

        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1]:
                mem[s] = min(mem[s], 1 + self.partition(s[i:], mem))
        return mem[s]

    def minCut(self, s: str) -> int:
        mem = defaultdict(lambda: float('inf'))

        return self.partition(s, mem)