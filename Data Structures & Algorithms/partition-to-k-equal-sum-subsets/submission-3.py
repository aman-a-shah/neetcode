class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort()

        target = sum(nums)/k
        if target != int(target):
            return False

        def dfs(curr_sum, subsets, used, start):
            if curr_sum == target:
                if subsets == k-1:
                    return True
                else:
                    return dfs(0, subsets + 1, used, 0)
            
            prev = -1
            acc = set()
            for i in range(start, len(nums)):
                if curr_sum + nums[i] <= target and i not in used and nums[i] != prev:
                    used.add(i)
                    if dfs(curr_sum + nums[i], subsets, used, i+1):
                        return True
                    used.remove(i)
                    prev = nums[i]
            
            return False
                    
        
        return dfs(0, 0, set(), 0)