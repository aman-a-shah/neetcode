from functools import cache

class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def dfs(i, stack):
            if i == len(s):
                return stack == 0

            if s[i] == '(':
                return dfs(i+1, stack+1)
            if s[i] == ')':
                stack -= 1
                if stack < 0:
                    return False
                return dfs(i+1, stack)
            if s[i] == '*':
                if dfs(i+1, stack):
                    return True
                if dfs(i+1, stack+1):
                    return True
                if dfs(i+1, stack-1):
                    return True
            return False


        return dfs(0, 0)