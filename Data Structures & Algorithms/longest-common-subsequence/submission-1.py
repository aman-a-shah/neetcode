class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # cat vs. crabt = cat
        # dp[i][j] <- longest substring with i char from text1, j char from text2

        """
                c   r   a   b   t
            0   0   0   0   0   0
        c   0   1   1   1   1   1
        a   0   1   1   2   2   2
        t   0   1   1   2   2   3
        """

        m, n = len(text1)+1, len(text2)+1

        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    continue
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]