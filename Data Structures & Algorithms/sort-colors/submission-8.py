class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zeros = 0
        twos = 0
        i = 0

        while i < len(nums)-twos:
            if nums[i] == 0:
                if zeros != i:
                    nums[i], nums[zeros] = nums[zeros], nums[i]
                zeros += 1
                i += 1
                continue
            if nums[i] == 2:
                nums[i], nums[len(nums)-1-twos] = nums[len(nums)-1-twos], nums[i]
                twos += 1
                continue
            if nums[i] == 1:
                i += 1