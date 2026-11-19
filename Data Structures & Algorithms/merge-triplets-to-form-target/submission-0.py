class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # find candidate for a (same as x) and b, c <= y, z
        # find candidate for b (same as y) and a, c <= x, z
        # find candidate for c (same as z) and a, b <= x, y
        # return found all
    
        candidates = [False, False, False]
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            if a == target[0]:
                candidates[0] = True
            if b == target[1]:
                candidates[1] = True
            if c == target[2]:
                candidates[2] = True
        return all(candidates)

        