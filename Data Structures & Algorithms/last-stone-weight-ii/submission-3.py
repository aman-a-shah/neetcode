from functools import cache

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # stone weights 
        # we smash stones - weights get substracted 
        # want to return min weight left

        target = sum(stones)//2
        res = sum(stones)
        
        @cache
        def top_down(i, sum_so_far):
            if sum_so_far > target:
                return
            if i >= len(stones):
                nonlocal res
                res = min(res, sum(stones)-(sum_so_far*2))
                return
            
            top_down(i+1, sum_so_far + stones[i])
            top_down(i+1, sum_so_far)

            
        top_down(0, 0)
        return res