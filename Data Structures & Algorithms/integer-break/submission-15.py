class Solution:
    def integerBreak(self, n: int) -> int:
        """
        8
        1 * 7 -> 1 * 6 * 1 -> 1 * 5 * 2 -> 1 * 4 * 3 = 12
        2 * 2 * 2 * 2 = 16

        9
        3^3 = 27
        
        10
        -> 3^3 *1
        """

        # 0 -> 0
        # 1 -> 0
        # 2 -> 1
        # 3 -> 2
        # 4 -> 4
        # 5 -> 6

        # 6 ->   (9)

        # dp[i] = max product for n==i
        # dp[i+1] = max(dp[i]*dp[1], dp[i-1]*[dp[2]], ...) - go to halfway point
 
        if n in {0, 1}:
            return 0
        if n == 2:
            return 1

        dp = [0] * (n+1)
        dp[0], dp[1] = 0, 0

        # [0, 0, 1, _]
        # [0, 0, 1, 2, _]        
        for i in range(3, n+1):
            for j in range(1, (i//2)+1):
                op = max(dp[j], j) * max(dp[i-j], i-j)
                dp[i] = max(dp[i], op)
        return dp[-1]


