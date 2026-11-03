class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        num_trust_me = [0] * n
        num_i_trust = [0] * n
        for a, b in trust:
            num_trust_me[b-1] += 1
            num_i_trust[a-1] += 1
        
        candidates = set()
        for i in range(n):
            if num_trust_me[i] == n-1 and num_i_trust[i] == 0:
                candidates.add(i)
            
        if len(candidates) == 1:
            return candidates.pop()+1
        return -1
