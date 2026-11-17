from math import sqrt

class Solution:
    def numSquares(self, n: int) -> int:
        # least num perfect square sum to n
        # dp[i] = least num squares to add to i
        
        
        dp = [i for i in range(n+1)]

        for i in range(1, n+1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[abs(j*j-i)]+1)
                j += 1
            
        return dp[n]
