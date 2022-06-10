# 746. Min Cost Climbing Stairs

# Solution 1: Easy
class Solution:
    def calcCost(self, cost, idx, dp):
        if idx in (0, 1):
            return cost[idx]
        
        if idx in dp:
            return dp[idx]
        
        dp[idx] = min(self.calcCost(cost, idx-1, dp), self.calcCost(cost, idx-2, dp)) + cost[idx]
        
        return dp[idx]
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        len_cost = len(cost)
        dp = dict()
        
        return min(self.calcCost(cost, len_cost-1, dp), self.calcCost(cost, len_cost-2, dp))