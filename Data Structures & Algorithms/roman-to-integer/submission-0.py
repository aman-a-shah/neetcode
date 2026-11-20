class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0 
        i = 0

        val = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        mp = {
            'I':{'V':4, 'X':9}, 
            'X':{'L':40, 'C':90}, 
            'C':{'D':400, 'M':900}
        }

        while i < len(s):
            if s[i] in mp:
                if i < len(s)-1 and s[i+1] in mp[s[i]]:
                    res += mp[s[i]][s[i+1]]
                    i += 2
                    continue
            res += val[s[i]]
            i += 1
            

        return res