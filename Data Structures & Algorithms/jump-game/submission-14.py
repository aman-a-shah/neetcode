from functools import cache

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        @cache
        def dfs(i):
            if i == len(nums)-1:
                return True
            if i > len(nums)-1:
                return False
            
            for j in range(1, nums[i]+1):
                if dfs(i+j):
                    return True
            return False

        return dfs(0)