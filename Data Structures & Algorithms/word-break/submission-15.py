class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # dp vers.
        dp = [False] * (len(s)+1)
        dp[0] = True

        for i in range(len(s)+1):
            for j in range(i):
                if not dp[j]:
                    continue
                if s[j:i] in wordDict:
                    dp[i] = True
                    continue

        return dp[len(s)]

        