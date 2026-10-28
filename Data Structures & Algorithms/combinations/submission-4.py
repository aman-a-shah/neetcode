class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # distinct subsets length k, 1-n
        acc = []

        def dfs(curr_n, subset):
            if len(subset) == k:
                if subset not in acc:
                    acc.append(subset.copy())
                return

            if curr_n > n or len(subset) > k:
                return
            
            dfs(curr_n+1, subset+[curr_n])
            dfs(curr_n+1, subset)

        dfs(1, [])
        return acc