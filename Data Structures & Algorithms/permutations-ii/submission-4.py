class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        acc = []
        used = [False] * len(nums)
        subset = []

        def dfs():
            if len(subset) == len(nums):
                acc.append(subset.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                # skip duplicate: if same value as previous and previous not used at this level
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = True
                subset.append(nums[i])
                dfs()
                subset.pop()
                used[i] = False

        dfs()
        return acc