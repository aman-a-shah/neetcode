class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zeros = 0
        twos = 0
        i = 0
        
        while i < len(nums) - twos:
            if nums[i] == 0:
                # Only swap if zeros != i (avoid swapping with itself)
                if zeros != i:
                    nums[i], nums[zeros] = nums[zeros], nums[i]
                zeros += 1
                i += 1  # Safe to increment because we're moving forward
            elif nums[i] == 2:
                target_idx = len(nums) - 1 - twos
                # Only swap if target_idx != i (avoid swapping with itself)
                if target_idx != i:
                    nums[i], nums[target_idx] = nums[target_idx], nums[i]
                twos += 1
                # DON'T increment i - need to check what came from the end
            else:  # nums[i] == 1
                i += 1