from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_f = max(freq.values())
        num_max = sum(1 for f in freq.values() if f == max_f)

        # Build frames of size (n+1) around the most frequent task(s)
        gaps = (max_f - 1) * (n + 1) + num_max
        return max(len(tasks), gaps)