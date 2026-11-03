from functools import cache
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        n = max(len(word) for word in dictionary)

        @cache
        def dfs(i):
            if i >= len(s):
                return 0

            # assume we skip
            best = dfs(i+1) + 1

            # don't
            cur = ''
            for j in range(n):
                if j+i >= len(s):
                    best = min(best, j+i)
                    break
                cur += s[j+i]
                if cur in dictionary:
                    best = min(best, dfs(i+j+1))
            
            return best
                
        return dfs(0)
