from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        @cache         
        def dp(i: int, holding: bool):
            if i >= len(prices):
                return 0
            best = dp(i + 1, holding)
            if holding:
                best = max(best, prices[i] + dp(i + 2, False))
            else:
                best = max(best, -prices[i] + dp(i + 1, True))
            return best
            
        return dp(0, False)