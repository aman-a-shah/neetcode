class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        less, more = (str1, str2) if len(str1) < len(str2) else (str2, str1)

        def divides(unit, s):
            if not unit or len(s) % len(unit) != 0:
                return False
            return unit * (len(s) // len(unit)) == s

        for length in range(len(less), 0, -1):   # stop at 1, not 0
            cand = less[:length]
            if divides(cand, str1) and divides(cand, str2):
                return cand
        return ""