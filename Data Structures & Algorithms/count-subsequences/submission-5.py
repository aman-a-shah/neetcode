from functools import cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # num seq in s that match t
        # for each let, we can choose to include or not

        @cache
        def dfs(i, j):
            if j == len(t):
                return 1
            if i >= len(s):
                return 0

            res = dfs(i+1, j)
            if s[i] == t[j]:
                res += dfs(i+1, j+1)

            return res

        return dfs(0, 0)
