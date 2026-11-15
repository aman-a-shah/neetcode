from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        sm = sum(nums)
        if sm % 2 == 1:
            return False
        target = sm//2
        memo = {} # (sum_so_far, i):res
        
        def backtrack(sum_so_far, i):
            if sum_so_far == target:
                return True
            if (sum_so_far, i) in memo:
                return memo[(sum_so_far, i)]
            if sum_so_far > target or i >= len(nums):
                memo[(sum_so_far, i)] = False
                return False

            pick = backtrack(sum_so_far + nums[i], i+1)
            skip = backtrack(sum_so_far, i+1)
            res = pick or skip

            memo[(sum_so_far, i)] = res 
            return res

        return backtrack(0, 0)
        