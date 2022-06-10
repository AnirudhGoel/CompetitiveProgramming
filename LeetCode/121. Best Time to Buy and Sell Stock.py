# 121. Best Time to Buy and Sell Stock

# Solution 1: O(n) 64% faster
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        profit = 0
        
        for i in range(len(prices)):
            if prices[i] > prices[buy]:
                profit = max(profit, prices[i] - prices[buy])
            else:
                buy = i
        
        return profit