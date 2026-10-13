class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # find rotated amount
        rot = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                rot = i

        # binary search on unrotated
        def helper(left: int, right: int):
            if left >= right:
                return nums[(left + rot)%len(nums)] == target
            
            mid = (left+right)//2
            index = (mid+rot)%len(nums)

            if nums[index] >= target:
                return helper(left, mid)
            else:
                return helper(mid+1, right)

        # find then true, else false
        return helper(0, len(nums)-1)