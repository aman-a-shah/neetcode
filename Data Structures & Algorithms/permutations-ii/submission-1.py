class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        acc = []

        def dfs(visited, subset):
            if len(subset) == len(nums):
                if subset not in acc:
                    acc.append(subset)
                return
            
            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    dfs(visited, subset + [nums[i]])
                    visited.remove(i)
            
        dfs(set(), [])
        return acc