from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @cache
        def dfs(i, j):
            # done p and done s?
            if j == len(p):
                return i == len(s)

            matching = False
            if i < len(s) and (p[j] == s[i] or p[j] == '.'):
                matching = True

            if j + 1 < len(p) and p[j + 1] == '*':
                k = i
                while True: 
                    if dfs(k, j + 2):   
                        return True
                    if k < len(s) and (p[j] == s[k] or p[j] == '.'):
                        k += 1          
                    else:
                        return False

            # matching pattern
            if i < len(s) and (p[j] == s[i] or p[j] == '.'):
                # same val so move forward
                return dfs(i+1, j+1)

            return False
        
        return dfs(0, 0)