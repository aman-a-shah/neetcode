from functools import cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def dfs(i1, i2):
            i = i1 + i2
            if i == len(s3):
                return True
            if i1 < len(s1) and s1[i1] == s3[i] and dfs(i1 + 1, i2):
                return True
            if i2 < len(s2) and s2[i2] == s3[i] and dfs(i1, i2 + 1):
                return True
            return False

        return dfs(0, 0)