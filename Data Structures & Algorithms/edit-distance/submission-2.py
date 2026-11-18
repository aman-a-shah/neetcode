from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dfs(i, j):
            if j >= len(word2):
                return len(word1)-i
            if i >= len(word1):
                return len(word2)-j
            if word1[i] == word2[j]:
                return dfs(i+1, j+1)
            
            # insert, delete, replace
            replace = dfs(i+1, j+1) + 1
            insert = dfs(i, j+1) + 1
            delete = dfs(i+1, j) + 1

            return min({replace, insert, delete})
        
        return dfs(0, 0)