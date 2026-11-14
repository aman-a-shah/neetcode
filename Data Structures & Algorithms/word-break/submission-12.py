class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # build up s using wors in wordDict?
        memo = {}
        def bt(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            
            for word in wordDict:
                if s.startswith(s[:i]+word):
                    b = bt(i+len(word))
                    memo[i+len(word)] = b
                    if b:
                        return True

            memo[i] = False
            return False
        
        return bt(0)
        
        
        
        # dp vers.
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break

        return dp[len(s)]

        