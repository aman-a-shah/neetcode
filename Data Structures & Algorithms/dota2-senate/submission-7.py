class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # phase 1: delete rights of nxt opposing senator
        # phase 2: if no one opposing left, announce success

        # return 'radiant' if d == 0 and vice versa

        # nums of senators
        s = len(senate)
        d = sum([1 for i in range(s) if senate[i] == 'D'])
        r = s-d
        
        # skips
        skip = set()

        i = 0
        while d > 0 and r > 0:
            idx = i % s
            if idx in skip:
                i += 1
                continue
            
            if senate[idx] == 'R':
                d -= 1
                for j in range(s):
                    skip_i = (idx+j+1)%s
                    if senate[skip_i] == 'D' and skip_i not in skip:
                        skip.add(skip_i)
                        break
            else:
                r -= 1
                for j in range(s):
                    skip_i = (idx+j+1)%s
                    if senate[skip_i] == 'R' and skip_i not in skip:
                        skip.add(skip_i)
                        break

            i += 1
        
        if d > 0:
            return 'Dire'
        else:
            return 'Radiant'