import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_sorted = []
        counts = Counter(s)

        for let, freq in counts.items():
            heapq.heappush(freq_sorted, [-freq, let])
        
        acc = ''
        last = None

        if -freq_sorted[0][0] > (len(s)+1)//2:
            return ''

        while freq_sorted:
            _ = heapq.heappop(freq_sorted)
            freq = _[0] + 1
            let = _[1]
            acc += let

            if last:
                heapq.heappush(freq_sorted, last)
            if freq != 0:
                last = [freq, let]
            else:
                last = None

        return acc
