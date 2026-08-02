class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}

        for wrd in strs:
            srt = ''.join(sorted(wrd))
            if srt in mp:
                mp[srt].append(wrd)
            else:
                mp[srt] = [wrd]
        
        return [mp[key] for key in mp]