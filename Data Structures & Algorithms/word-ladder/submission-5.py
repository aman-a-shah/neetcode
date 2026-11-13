from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if beginWord == endWord:
            return 1
        
        def one_let_off(n1, n2):
            allow = True
            for i in range(len(n1)):
                if n1[i] == n2[i]:
                    continue
                if allow:
                    allow = False
                    continue
                else:
                    return False
            return True

        # 1. build graph
        graph = {word:[] for word in wordList}
        graph[beginWord] = []

        for node in graph:
            for word in wordList:
                if one_let_off(node, word):
                    graph[node].append(word)

        # 2. bfs from beginWord to endWord
        visited = set()
        res = 1
    
        q = deque([(beginWord, 1)])
        while q:
            node, wrds = q.popleft()
            visited.add(node)

            if node == endWord:
                return wrds

            for n in graph[node]:
                if n not in visited:
                    q.append((n, wrds+1))

        return 0






