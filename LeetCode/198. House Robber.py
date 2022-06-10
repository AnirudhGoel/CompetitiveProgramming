# 198. House Robber

# Solution 1: On my own, first attempt
class Solution:
    def money(self, nums, house_idx, dp):
        if house_idx >= len(nums):
            return 0
        
        if house_idx in dp:
            return dp[house_idx]
        
        dp[house_idx] = max(self.money(nums, house_idx + 2, dp) + nums[house_idx], self.money(nums, house_idx + 1, dp))
        
        return dp[house_idx]
    
    def rob(self, nums: List[int]) -> int:
        dp = dict()
        
        return self.money(nums, 0, dp)