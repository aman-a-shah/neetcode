class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bst(lst: list):
            mid = len(lst) // 2
            if lst[mid] == target:
                return mid
            if len(lst) == 1:
                return -1
            
            if target < lst[mid]:
                return bst(lst[:mid])
            else:
                top = bst(lst[mid:])
                return mid + top if top != -1 else top
            
        return bst(nums)