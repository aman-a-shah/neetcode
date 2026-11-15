from math import sqrt

class Solution:
    def numSquares(self, n: int) -> int:
        # least num perfect square sum to n
        # dp[i] = least num squares to add to i
        
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        
        for i in range(len(dp)):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], 1 + dp[i - j * j])
                j += 1
        
        return dp[-1]