class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        acc = []

        def dfs(visited, subset):
            if len(subset) == len(nums):
                if subset not in acc:
                    acc.append(subset)
                return
            
            i = 0
            while i < len(nums):
                if i not in visited:
                    visited.add(i)
                    dfs(visited, subset + [nums[i]])
                    visited.remove(i)
                
                    while i+1 < len(nums) and nums[i] == nums[i+1]:
                        i += 1
                i += 1

        dfs(set(), [])
        return acc