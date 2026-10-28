class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        acc = []
        candidates.sort()

        def dfs(i, subset, sm):
            nonlocal acc

            if sm == target: # success
                acc.append(subset.copy())
                return
 
            if i >= len(candidates) or sm+candidates[i] > target: # failure
                return
            
            subset.append(candidates[i])
            dfs(i + 1, subset, sm + candidates[i])
            subset.pop()
            
            j = i
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j, subset, sm)

        dfs(0, [], 0)
        return acc