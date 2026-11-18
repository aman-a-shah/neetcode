from functools import cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # num seq in s that match t
        # for each let, we can choose to include or not

        @cache
        def dfs(i, acc):
            if acc == t:
                return 1
            if i >= len(s):
                return 0

            return dfs(i+1, acc+s[i]) + dfs(i+1, acc)

        return dfs(0, '')
