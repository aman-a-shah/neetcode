from functools import cache

class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        A = [1] + nums + [1]
        n = len(A)
        
        @cache
        def solve(l: int, r: int) -> int:
            # Max coins from bursting ALL balloons strictly between l and r.
            # Balloons l and r themselves are NOT burst.
            if r - l <= 1:
                return 0  # nothing between them

            best = 0
            # Try each balloon k as the LAST balloon burst between l and r
            for k in range(l + 1, r):
                coins = (
                    solve(l, k)             # burst everything between l and k
                    + solve(k, r)           # burst everything between k and r
                    + A[l] * A[k] * A[r]    # then finally burst k
                )
                best = max(best, coins)

            return best

        return solve(0, n - 1)