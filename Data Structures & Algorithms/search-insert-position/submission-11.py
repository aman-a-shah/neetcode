class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def helper(lst: list):
            if len(lst) == 1:
                if lst[0] >= target:
                    return 0
                else:
                    return 1
            
            mid = len(lst)//2
            
            if lst[mid] == target:
                return mid
            elif lst[mid] > target:
                return helper(lst[:mid])
            else:
                return mid + helper(lst[mid:])

        return helper(nums)