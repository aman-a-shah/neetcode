class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = 0
        acc = 0

        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
                acc += 1

        return acc
        