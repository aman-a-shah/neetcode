from collections import Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # expand window - can only stop when reach end or all lets fully accounted for
        counts = Counter(s)
        cur_win = set()
        win_size = 0
        count = 0

        res = []

        for i in range(len(s)):
            counts[s[i]] -= 1
            if s[i] in cur_win:
                count -= 1
            else:
                count += counts[s[i]]
            win_size += 1
            
            cur_win.add(s[i])
            if count == 0:
                res.append(win_size)
                cur_win = set()
                win_size = 0

            counts[s[i]] -= 1
    
        if cur_win:
            res.append(win_size)
        
        return res