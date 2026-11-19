class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_turb = 0
        cur_turb = 0
        if len(arr) < 2:
            return 1
        gt = arr[1] < arr[0]

        for i in range(len(arr)-1):
            if (gt and arr[i] > arr[i+1]) or (not gt and arr[i] < arr[i+1]):
                cur_turb += 1
                max_turb = max(max_turb, cur_turb)
            else:
                cur_turb = 1 if arr[i+1] != arr[i] else 0
                gt = arr[i+1] < arr[i] 

            gt = not gt
            max_turb = max(max_turb, cur_turb)    

        return max_turb+1