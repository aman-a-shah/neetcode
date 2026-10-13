class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        comb = nums1+nums2
        comb.sort()
        if len(comb) == 0:
            return 0
        if len(comb) == 1:
            return comb[0]

        if len(comb) % 2 == 0:
            return (comb[len(comb)//2-1] + comb[(len(comb)//2)]) / 2
        else:
            return comb[len(comb)//2]