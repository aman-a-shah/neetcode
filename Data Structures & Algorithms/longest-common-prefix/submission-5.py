class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]

        for wrd in strs:
            if len(wrd) < len(common):
                common = common[:len(wrd)]
            for i, let in enumerate(wrd):
                if i >= len(common) or common[i] != wrd[i]:
                    common = wrd[:i]
                    break
                
        
        return common