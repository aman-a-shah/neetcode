from collections import defaultdict, deque

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # prime factorize & create index_primes and primes_index
        # bfs through graph if connected then True
        # handle case where if 1, return False

        # base
        if 1 in nums:
            return nums==[1]

        # prime factorize
        def get_primes(n):
            prime = [True]*(n+1)
            prime[0], prime[1] = False, False
            res = set()

            for i in range(n+1):
                if not prime[i]:
                    continue
                
                res.add(i)
                mult = i+i
                while mult <= n:
                    prime[mult] = False
                    mult += i

            return res
        
        def prime_factor(n):
            res = set()

            while n > 1:
                for i in range(len(primes)):
                    
                    if n % primes[i] == 0:
                        n = n // primes[i]
                        res.add(primes[i])
                        break
            
            return res
        
        # index_primes + primes_index
        primes = list(get_primes(max(nums)))
        index_primes = {i:[] for i in range(len(nums))}
        primes_index = defaultdict(list)
        
        for i in range(len(nums)):
            factor = prime_factor(nums[i])
            index_primes[i] = list(factor)
            for prime in factor:
                primes_index[prime].append(i)
            
        # graph traversal - connected?
        q = deque([index_primes[0][0]])
        visited = set()
        while q:
            prime = q.popleft()
            if prime in visited:
                continue
            visited.add(prime)
            for idx in primes_index[prime]:
                for p in index_primes[idx]:
                    if p not in visited:
                        q.append(p)
        
        return len(visited) == len(primes_index)




