class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        less, more = (str1, str2) if len(str1) < len(str2) else (str2, str1)
        
        if less != more[0:len(less)]:
            return ''
        
        def divides(unit, s):
            acc = unit
            while len(acc) < len(s):
                acc += unit
            return acc == s
                
        for i in range(len(less), 0, -1):
            if divides(less[:i], less) and divides(less[:i], more):
                return less[:i]
        
        return ''
