class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        acc = []
        
        def dfs(start, subset):
            acc.append(subset[:])                 # every node is a valid subset
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue                       # skip dup at same level
                subset.append(nums[i])
                dfs(i + 1, subset)
                subset.pop()
        
        dfs(0, [])
        return acc