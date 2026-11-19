from collections import Counter
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        heap = list(count.keys())
        heapq.heapify(heap)

        while heap:
            strt = heap[0]
            for card in range(strt, strt+groupSize):
                if count[card] == 0:
                    return False
                count[card] -= 1
                if count[card] == 0:
                    if card != heap[0]:
                        return False
                    heapq.heappop(heap)
                
        return True