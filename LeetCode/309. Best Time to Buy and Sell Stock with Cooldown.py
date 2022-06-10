# 309. Best Time to Buy and Sell Stock with Cooldown

class Solution:
    def calcProfit(self, prices, day, bought, profit):
        if day >= len(prices) - 1:
            if bought:
                return profit + prices[day]
            else:
                return profit
        
        if bought:
            return max(self.calcProfit(prices, day+2, False, profit+prices[day]), 
                      self.calcProfit(prices, day+1, True, profit))
        else:
            return max(self.calcProfit(prices, day+1, True, profit-prices[day]),
                      self.calcProfit(prices, day+1, False, profit))
    
    def maxProfit(self, prices: List[int]) -> int:
        return self.calcProfit(prices, 0, False, 0)