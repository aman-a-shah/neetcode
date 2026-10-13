class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l, r = 0, 0
        result = float('inf')
        cur_sum = 0

        for r in range(len(nums)):
            cur_sum += nums[r]

            while cur_sum >= target and l <= r:
                result = min(result, r-l+1)
                cur_sum -= nums[l] 
                l += 1

        if isinstance(result, int):
            return result
        else:
            return 0