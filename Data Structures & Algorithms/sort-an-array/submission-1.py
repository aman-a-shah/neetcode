class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # insertion 
        for i, n in enumerate(nums):
            
            index = i
            while index > 0 and n < nums[index-1]:
                nums[index], nums[index-1] = nums[index-1], n
                index -= 1
        
        return nums