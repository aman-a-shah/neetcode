class Solution:
    def maxSubarraySumCircular(self, nums):

        cur_min, glo_min = float('inf'), float('inf')
        cur_max, glo_max = float('-inf'), float('-inf')

        total = sum(nums)

        for i in range(len(nums)):
            cur_min = nums[i] if cur_min > 0 else cur_min + nums[i]
            glo_min = min(glo_min, cur_min)

            cur_max = nums[i] if cur_max < 0 else cur_max + nums[i]
            glo_max = max(glo_max, cur_max)
        
        if glo_max < 0:
            return glo_max
        return max(total-glo_min, glo_max)
