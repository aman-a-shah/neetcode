class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == '':
            return []

        acc = []
        mp = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def dfs(i, wrd):
            if len(wrd) == len(digits):
                acc.append(wrd)
                return
            
            for let in mp[digits[i]]:
                dfs(i+1, wrd + let)
        
        dfs(0, '')
        return acc