class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        # backtrack

        # keep adding until we get sum, cut off if larger
        memo = {}
        def backtrack(sum_so_far):
            if sum_so_far == target:
                return 1
            elif sum_so_far > target:
                return 0
            if sum_so_far in memo:
                return memo[sum_so_far]
            
            acc = 0
            for num in nums:
                temp = backtrack(sum_so_far + num)
                memo[sum_so_far + num] = temp
                acc += temp
            return acc
                
        return backtrack(0)

        # dp
        dp = [0] * (target + 1)
        dp[0] = 1
        for r in range(1, target + 1):
            for num in nums:
                if num <= r:
                    dp[r] += dp[r - num]
        return dp[target]