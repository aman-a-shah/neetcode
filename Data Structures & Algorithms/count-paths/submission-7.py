import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # ((m+n-2) (n-1))
        # (m+n-2)! / ((n-1)!)^2
        
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]

        return math.factorial(m+n-2) // (math.factorial(n-1) * math.factorial(m-1))

