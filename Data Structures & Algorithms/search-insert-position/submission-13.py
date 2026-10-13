class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def helper(left: int, right: int) -> int:
            if left > right:
                return left
            
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return helper(left, mid - 1)
            else:
                return helper(mid + 1, right)
        
        return helper(0, len(nums) - 1)