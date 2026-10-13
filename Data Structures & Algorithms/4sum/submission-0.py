class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 3):
            # Skip duplicates for i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i + 1, n - 2):
                # Skip duplicates for j
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                # Two-pointer on remaining array
                left = j + 1
                right = n - 1
                remaining_target = target - nums[i] - nums[j]
                
                while left < right:
                    current_sum = nums[left] + nums[right]
                    
                    if current_sum == remaining_target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        
                        # Skip duplicates for left
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        # Skip duplicates for right
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                            
                    elif current_sum < remaining_target:
                        left += 1
                    else:
                        right -= 1
        
        return result