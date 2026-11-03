class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        acc = []
        n = max(len(word) for word in wordDict)

        def backtrack(sentence, i):
            if i >= len(s):
                acc.append(sentence)

            curr = ''
            for j in range(n):
                if j+i >= len(s):
                    break
                curr += s[j+i]
                if curr in wordDict:
                    backtrack(sentence + [curr], j+i+1)
                

        backtrack([], 0)
        for i in range(len(acc)):
            acc[i] = ' '.join(acc[i])

        return acc