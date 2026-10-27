import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        acc = ''

        freq_let = []
        if a: heapq.heappush(freq_let, [-a, 'a'])
        if b: heapq.heappush(freq_let, [-b, 'b'])
        if c: heapq.heappush(freq_let, [-c, 'c'])

        unusable = []

        while freq_let:

            element = heapq.heappop(freq_let)
            freq = element[0]
            let = element[1]

            acc += let 
            freq += 1

            if unusable != []: 
                heapq.heappush(freq_let, unusable)
                unusable = []

            if freq:
                if acc[-2:] == let*2:
                    unusable = [freq, let]
                else:
                    heapq.heappush(freq_let, [freq, let])

        return acc
        

