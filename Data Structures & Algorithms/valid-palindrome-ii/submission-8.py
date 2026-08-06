class Solution:
    def validPalindrome(self, s: str) -> bool:

        if s == s[::-1]:
            return True

        for i in range(0, len(s)):
            temp = s[0:i]+s[i+1:]
            if temp == temp[::-1]:
                return True
        return False


