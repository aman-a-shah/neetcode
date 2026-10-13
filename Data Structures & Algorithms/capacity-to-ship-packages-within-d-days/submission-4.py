class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def check(max_weight):
            count = 0
            cur_count = 0

            for weight in weights:
                if cur_count + weight <= max_weight:
                    cur_count += weight
                else:
                    count += 1
                    cur_count = weight
                
                if count > days:
                    return False
            
            count += 1
            if count > days:
                return False

            return True

        def helper(left:int, right:int):
            if left >= right:
                return left
            
            mid = (left+right)//2

            if check(mid):
                return helper(left, mid)
            else:
                return helper(mid+1, right)
        
        return helper(max(weights), sum(weights))
        