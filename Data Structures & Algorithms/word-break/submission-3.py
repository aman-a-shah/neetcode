from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # can you build s with words from wordDict

        @cache
        def backtrack(wrd):
            if len(wrd) > len(s):
                return False
            if wrd == s:
                return True
            for nxt in wordDict:
                if wrd+nxt == s[:len(wrd+nxt)]:
                    if backtrack(wrd+nxt):
                        return True
            return False
        return backtrack('')