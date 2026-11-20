class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        
        while y:
            carry = (x & y) << 1
            x = x ^ y
            y = carry

        return bin(x)[2:]