# 122. Best Time to Buy and Sell Stock II

# Solution 1: Simple Greedy Solution, just buy and sell on each pair of days where day 1 price < day 2 price. We do not have any transaction limit or fee.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        
        return profit