from functools import cache

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)

        @cache
        def dfs(i):
            if i == n-1:
                return 0
            if i > n-1:
                return n
            
            acc = float('inf')
            for j in range(1, nums[i]+1):
                acc = min(acc, dfs(i+j))
            return acc+1

        return dfs(0)