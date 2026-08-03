from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        acc = []

        for key in counts:
            if counts[key] > int(len(nums)/3):
                acc.append(key)

        return acc