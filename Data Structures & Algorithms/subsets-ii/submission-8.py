class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        acc = []
        
        def dfs(start, subset):
            acc.append(subset[:])                 
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue                       
                subset.append(nums[i])
                dfs(i + 1, subset)
                subset.pop()
        
        dfs(0, [])
        return acc