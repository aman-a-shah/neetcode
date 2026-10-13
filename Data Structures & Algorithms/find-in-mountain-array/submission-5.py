class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
      
        # find peak
        left, right = 0, mountainArr.length()-1
        peak = -1
        while left < right:
            mid = (left + right) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peak = left

        if peak == -1:
            return -1 # no peak

        # check left half of mountain
        left, right = 0, peak
        while left <= right:
            mid = (left + right) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # check right half
        left, right = peak, mountainArr.length()-1
        while left <= right:
            mid = (left + right) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

        
