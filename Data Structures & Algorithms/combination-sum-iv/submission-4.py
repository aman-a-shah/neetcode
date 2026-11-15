class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        # dp[i] = num combinations add to i
        dp = [0] * (target+1)
        dp[0] = 1

        for i in range(1, len(dp)):
            for num in nums:
                if num <= i and dp[i-num]:
                    dp[i] += dp[i-num]
        
        return dp[-1]


        
        