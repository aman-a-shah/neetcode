from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for let in counts:
            if counts[let] > len(nums)/2:
                return let