class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # travel backwards nth stone to 1st
        # have each 

        n = len(stoneValue)
        dp = [0] * (n + 1)          # dp[n] = 0 by default

        for i in range(n - 1, -1, -1):
            take = 0
            best = float('-inf')
            for k in range(1, 4):           # take 1, 2, or 3 stones
                if i + k > n:
                    break
                take += stoneValue[i + k - 1]
                best = max(best, take - dp[i + k])
            dp[i] = best

        if dp[0] > 0:  return "Alice"
        if dp[0] < 0:  return "Bob"
        return "Tie"