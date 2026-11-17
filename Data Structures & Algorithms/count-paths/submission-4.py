import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # ((m+n-2) (n-1))
        # (m+n-2)! / ((n-1)!)^2
        return math.factorial(m+n-2) // (math.factorial(n-1) * math.factorial(m-1))

