class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # two pointer
        ar1, ar2 = 0, 0
        n1 = nums1.copy()
        i = 0

        while ar1 < m and ar2 < n:
            if n1[ar1] < nums2[ar2]:
                nums1[i] = n1[ar1]
                ar1 += 1
            else:
                nums1[i] = nums2[ar2]
                ar2 += 1
            i += 1

        for j in range(ar1, m):
            nums1[i] = n1[j]
            i += 1
        for j in range(ar2, n):
            nums1[i] = nums2[j]
            i += 1
    
