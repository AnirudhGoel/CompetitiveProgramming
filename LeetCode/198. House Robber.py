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

# Solution 2: Wrote myself after understanding (check iPad for logic flow)
# T: O(N), S: O(N)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        dp = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            dp.append(max(dp[i-2] + nums[i], dp[i-1]))

        return dp[-1]

# Solution 3: Again on my own! YAY!
# T: O(N), S: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        second_last, last = nums[0], max(nums[0], nums[1])

        curr = last

        for i in range(2, len(nums)):
            curr = max(second_last + nums[i], last)
            second_last = last
            last = curr

        return curr