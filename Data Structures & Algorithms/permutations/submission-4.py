class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        acc = []

        def dfs(subset):
            if len(subset) > len(nums):
                return 

            if len(subset) == len(nums):
                acc.append(subset.copy())
                return
            
            for num in nums:
                if num not in subset:
                    dfs(subset+[num])

        dfs([])
        return acc