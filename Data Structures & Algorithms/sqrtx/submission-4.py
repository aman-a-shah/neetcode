class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 0:
            return 0

        def helper(left: int, right: int):
            if left >= right:
                return left
            
            mid = (left+right)//2

            if mid**2 == x:
                return mid
            elif mid**2 < x:
                if (mid+1)**2 > x:
                    return mid
                return helper(mid+1, right)
            else:
                return helper(left, mid-1)

        return helper(1, x)