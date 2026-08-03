class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        seen = {0: 1} # sum : num of occurences
        count = 0
        sum_so_far = 0
    
        for i, n in enumerate(nums):
            sum_so_far += n

            if sum_so_far - k in seen:
                count += seen[sum_so_far - k]
            
            if sum_so_far in seen:
                seen[sum_so_far] += 1
            else:
                seen[sum_so_far] = 1

        return count