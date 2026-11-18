class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        # Add virtual balloons with value 1 on both ends
        A = [1] + nums + [1]
        n = len(A)

        # dp[l][r] = max coins from bursting all balloons strictly between l and r
        dp = [[0] * n for _ in range(n)]

        # Length is the distance between boundaries l and r
        for length in range(2, n):
            for l in range(0, n - length):
                r = l + length
                for k in range(l + 1, r):
                    coins = (
                        dp[l][k]
                        + dp[k][r]
                        + A[l] * A[k] * A[r]
                    )
                    dp[l][r] = max(dp[l][r], coins)

        return dp[0][n - 1]