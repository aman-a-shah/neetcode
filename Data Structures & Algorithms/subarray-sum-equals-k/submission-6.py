class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # sum : # occurences
        count = 0
        seen = {0: 1}
        current_sum = 0

        for i, n in enumerate(nums):
            current_sum += n

            if current_sum - k in seen:
                count += seen[current_sum - k]

            if current_sum in seen:
                seen[current_sum] += 1
            else:
                seen[current_sum] = 1
        
        return count
