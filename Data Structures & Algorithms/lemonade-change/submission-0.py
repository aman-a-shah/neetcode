class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        mp = {5:0, 10:0, 20:0}

        for bill in bills:
            if bill == 5:
                mp[5] += 1
            elif bill == 10:
                if mp[5] == 0:
                    return False
                else:
                    mp[5] -= 1
                mp[10] += 1
            else:
                if mp[10] >= 1 and mp[5] >= 1:
                    mp[10] -= 1
                    mp[5] -= 1
                elif mp[5] >= 3:
                    mp[5] -= 3
                else:
                    return False
                mp[20] += 1
        
        return True