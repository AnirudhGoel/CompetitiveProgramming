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