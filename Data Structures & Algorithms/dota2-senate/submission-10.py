from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # phase 1: delete rights of nxt opposing senator
        # phase 2: if no one opposing left, announce success

        # return 'radiant' if d == 0 and vice versa

        s = len(senate)
        r = deque([i for i in range(s) if senate[i] == 'R'])
        d = deque([i for i in range(s) if senate[i] == 'D'])

        while r and d:
            r_i = r.popleft()
            d_i = d.popleft()

            if r_i < d_i:
                r.append(r_i + s)
            else:
                d.append(d_i + s)
        
        return 'Radiant' if r else 'Dire'

