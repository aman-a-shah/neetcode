from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if '0000' in deadends:
            return -1

        q = deque([('0000', 0)])
        memo = {'0000'}

        while q:
            code, dist = q.popleft()
            if code == target:
                return dist
            for i in range(4):
                digit = int(code[i])

                left = (digit-1)%10
                right = (digit+1)%10

                nxt_l = code[:i] + str(left) + code[i+1:]
                nxt_r = code[:i] + str(right) + code[i+1:]

                if nxt_l not in memo and nxt_l not in deadends:
                    q.append((nxt_l, dist+1))
                    memo.add(nxt_l)
                if nxt_r not in memo and nxt_r not in deadends:
                    q.append((nxt_r, dist+1))
                    memo.add(nxt_r)
        return -1        

