class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        alphabet = {}
        for i in range(len(order)):
            alphabet[order[i]] = i

        def ordered(str1, str2):
            for i in range(min(len(str1), len(str2))):
                if alphabet[str1[i]] > alphabet[str2[i]]:
                    return False
                if alphabet[str1[i]] == alphabet[str2[i]]:
                    continue
                if alphabet[str1[i]] < alphabet[str2[i]]:
                    return True
                
            return len(str1) <= len(str2)

        for i in range(len(words)-1):
            if not ordered(words[i], words[i+1]):
                return False
        return True
        
