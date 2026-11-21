class Solution:
    def minEnd(self, n: int, x: int) -> int:
        current_num = x
        remaining_count = n - 1

        bit_pos = 0
        while remaining_count > 0:
            if (x >> bit_pos) & 1 == 0:
                if (remaining_count & 1) == 1:
                    current_num |= (1 << bit_pos)
                remaining_count >>= 1
            bit_pos += 1
        return current_num