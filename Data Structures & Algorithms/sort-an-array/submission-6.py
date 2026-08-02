class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort
        def merge(lst: list) -> list:
            
            if len(lst) == 1:
                return lst

            mid = len(lst)//2

            left = merge(lst[:mid])
            right = merge(lst[mid:])

            acc = []
            l, r = 0, 0
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    acc.append(left[l])
                    l += 1
                else:
                    acc.append(right[r])
                    r += 1
            
            if left:
                for i in range(l, len(left)):
                    acc.append(left[i])
            if right:
                for i in range(r, len(right)):
                    acc.append(right[i])
            
            return acc

        return merge(nums)