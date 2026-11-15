from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        sm = sum(nums)
        if sm % 2 == 1:
            return False
        target = sm//2

        @cache
        def backtrack(sum_so_far, i):
            if sum_so_far == target:
                return True
            if sum_so_far > target:
                return False
            if i >= len(nums):
                return False

            pick = backtrack(sum_so_far + nums[i], i+1)
            skip = backtrack(sum_so_far, i+1)

            return pick or skip

        return backtrack(0, 0)
        