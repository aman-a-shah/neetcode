class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        
        i = 1
        while i in nums:
            i += 1
        return i


        lst = []

        for num in nums:
            if num < 1:
                continue
            if len(lst) < num:
                lst += [False] * (num-len(lst))
            lst[num-1] = True
        
        for i in range(len(lst)):
            if lst[i] == False:
                return i + 1
        
        return len(lst)
