from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        res = 0
        
        @cache
        def dp(amt_so_far, idx):
            if amt_so_far > amount:
                return 0
            if amt_so_far == amount:
                return 1
            acc = 0
            for i in range(idx, len(coins)):
                acc += dp(amt_so_far + coins[i], i)
            return acc
        
        return dp(0, 0)