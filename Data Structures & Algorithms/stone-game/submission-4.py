from functools import cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        @cache
        def dp(l, r, sm):
            if l > r:
                return sm > sum(piles)/2
            return dp(l+1, r, sm+piles[l]) or dp(l, r-1, sm+piles[r])
        
        return dp(0, len(piles)-1, 9)