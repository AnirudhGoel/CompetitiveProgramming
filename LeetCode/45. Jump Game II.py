# 45. Jump Game II

# My Approach 1: O(n^2)
class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = [float('inf')] * len(nums)
        steps[-1] = 0
        
        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= len(nums) - 1 - i:
                # if the current value > remaining indexes on the right, we can reach the last step in 1 jump
                steps[i] = 1
            elif nums[i] == 0:
                # if the current value == 0, we cannot move forward from this step
                steps[i] = float('inf')
            else:
                # else calculate the minimum of all the steps that can be reached from the current position
                steps[i] = min(steps[ i+1 : i+nums[i]+1 ]) + 1
        
        return steps[0]