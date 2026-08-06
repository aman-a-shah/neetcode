class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        acc = ''
        for i in range(min(len(word1), len(word2))):
            acc += word1[i]
            acc += word2[i]
        
        if len(word1) > len(word2):
            acc += word1[len(word2):]
        else:
            acc += word2[len(word1):]
        
        return acc
