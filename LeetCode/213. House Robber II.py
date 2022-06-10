# 213. House Robber II

# Solution 1: Recursion with memoization
class Solution:
    def money(self, nums, h_idx, dp):
        if h_idx >= len(nums):
            return 0
        
        if h_idx in dp:
            return dp[h_idx]
        
        dp[h_idx] = max(self.money(nums, h_idx + 2, dp) + nums[h_idx], self.money(nums, h_idx + 1, dp))
        
        return dp[h_idx]
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1: return nums[0]
        
        return max(self.money(nums[1:], 0, {}), self.money(nums[:n-1], 0, {}))