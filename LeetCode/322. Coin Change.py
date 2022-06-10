# 322. Coin Change

# Solution 1: Solved on my own! 40% faster!
class Solution:
    def calcChange(self, coins, amount, mem, curr_coin=None):
        # Base Case 1
        if amount == 0:
            return 0
        
        # Base Case 2
        if curr_coin and curr_coin > amount:
            return float('inf')
        
        # Memoization
        if amount in mem:
            return mem[amount]
        
        # Core Logic
        curr_min_num_coins = float('inf')
        for coin in coins:
            curr_num_coins = self.calcChange(coins, amount-coin, mem, coin)
            curr_min_num_coins = min(curr_min_num_coins, curr_num_coins)
            
        mem[amount] = curr_min_num_coins + 1
        return mem[amount]
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount: return 0
        
        mem = dict()

        num_coins = self.calcChange(coins, amount, mem)
        
        return -1 if num_coins == float('inf') else num_coins