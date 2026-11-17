class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # want to minimize sum 
        m, n = len(grid), len(grid[0])
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]

        acc = 0
        for i in range(m):
            acc += grid[i][0]
            dp[i][0] = acc
        acc = 0
        for i in range(n):
            acc += grid[0][i]
            dp[0][i] = acc
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[-1][-1]