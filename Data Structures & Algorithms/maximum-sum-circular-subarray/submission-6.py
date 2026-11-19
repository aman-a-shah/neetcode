class Solution:
    def maxSubarraySumCircular(self, nums):
        total = sum(nums)

        cur_max = best_max = nums[0]   # Kadane for max
        cur_min = best_min = nums[0]   # Kadane for min

        for x in nums[1:]:
            cur_max = max(x, cur_max + x)
            best_max = max(best_max, cur_max)

            cur_min = min(x, cur_min + x)
            best_min = min(best_min, cur_min)

        # If everything is negative, total - best_min = 0 (empty subarray),
        # which is illegal — the wrap case is meaningless here.
        if best_max < 0:
            return best_max

        return max(best_max, total - best_min)