class Solution:
    def integerBreak(self, n: int) -> int:
        # break n into nums s.t. sum(nums) = n, maximize prod(nums)

        # 0 -> 0 * 0 -> 0
        # 1 -> 1 * 0 -> 0
        # 2 -> 1 * 1 -> 1
        # 3 -> 1 * 1 * 1 = 1,       2 * 1 = 2
        # 4 -> 1 * 1 * 1 * 1 = 1,   2 * 2 = 4       3 * 1 = 3
        # 5 -> 1 * 1 * ... = 1,     3 * 2 = 6       4 * 1 = 4
        # 6 -> 1 * 1 * ... = 1,     4 * 2 = 8       3 * 3 = 9

        # dp[i] = max prod of num i
        # dp[i+1] = dp[j] * dp[i-j]

        dp = [1] * (n+1)
        dp[0], dp[1] = 0, 0

        for i in range(3, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(j, dp[j]) * max(i-j, dp[i-j]))
        return dp[n]
