from functools import cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        @cache
        def dp(alice, i, m):
            if i == len(piles):
                return 0
            
            acc = 0 if alice else float('inf')
            total = 0
            for x in range(1, 2*m+1):
                if i + x > len(piles):
                    break
                total += piles[i+x-1]
                res = dp(not alice, i+x, max(m, x))

                if alice:
                    acc = max(acc, res+total) 
                else:
                    acc = min(acc, res)
                    
            return acc
        
        return dp(True, 0, 1)