class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = strs[0]
        
        # Compare with every other word
        for word in strs[1:]:
            # Keep removing characters from the end
            # until prefix is a prefix of the current word
            while word[:len(prefix)] != prefix:
                prefix = prefix[:-1]  # Remove last character
                if not prefix:
                    return ""
        
        return prefix