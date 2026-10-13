class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # split into k subarrays
        # min possible largest sum

        def can_split(max_val):
            # can we get split where max_sum <= max_val
            subs = 1
            cur_sum = 0

            for i in range(len(nums)):
                if cur_sum + nums[i] > max_val:
                    cur_sum = nums[i]
                    subs += 1
                else:
                    cur_sum += nums[i]
                
                if subs > k:
                    return False
            
            return True

        def helper(left: int, right: int) -> int:
            if left >= right:
                return left

            mid = (left + right) // 2

            if can_split(mid):
                return helper(left, mid)
            else:
                return helper(mid+1, right)

            # check if mid possible
            # if mid possible to be max sum, then all [mid, right] possible and want to navigate to left otherwise to right
        
        return helper(max(nums), sum(nums))