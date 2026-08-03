class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        seen = {0: 1}  # prefix sum 0 seen once (empty subarray)
        
        for num in nums:
            current_sum += num  # this is prefix[j+1]
            
            # How many times have we seen (current_sum - k) before?
            if current_sum - k in seen:
                count += seen[current_sum - k]
            
            # Record that we've seen this prefix sum
            seen[current_sum] = seen.get(current_sum, 0) + 1
        
        return count