class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        
        while i < len(nums)-1:
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                nums.pop(i+1)
            i += 1

        return len(nums)

