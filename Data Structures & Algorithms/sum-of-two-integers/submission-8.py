class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  # 32 bits of 1

        a &= MASK
        b &= MASK

        while b:
            carry = ((a & b) << 1) & MASK
            a = (a ^ b) & MASK
            b = carry

        # Convert 32-bit unsigned result back to signed int
        return a if a < 0x80000000 else ~(a ^ MASK)