# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        def helper(left: int, right: int):
            if left == right:
                return left
            
            mid = (left + right) // 2

            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                return helper(left, mid-1)
            elif guess(mid) == 1:
                return helper(mid+1, right)

        return helper(1, n)
        