from collections import Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # expand window - can only stop when reach end or all lets fully accounted for
        counts = Counter(s)
        cur_win = []
        count = 0

        res = []

        for i in range(len(s)):
            if s[i] in cur_win:
                counts[s[i]] -= 1
                count -= 1
            else:
                counts[s[i]] -= 1
                count += counts[s[i]]
            cur_win.append(s[i])
            if count == 0:
                res.append(len(cur_win))
                cur_win = []

            counts[s[i]] -= 1
    
        if cur_win:
            res.append(len(cur_win))
        
        return res