class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(node, visited, i, j):
            nonlocal acc

            if node.word and not node.found:
                acc.append(node.word)
                node.found = True
            
            if (i, j) in visited or i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return

            if board[i][j] not in node.children:
                return

            cur = node.children[board[i][j]]
            visited.add((i, j))
            
            dfs(cur, visited.copy(), i-1, j)
            dfs(cur, visited.copy(), i+1, j)
            dfs(cur, visited.copy(), i, j-1)
            dfs(cur, visited.copy(), i, j+1)

        # 1. fill in tree
        root = TrieNode()

        for word in words:
            curr = root
            for let in word:
                if let not in curr.children:
                    curr.children[let] = TrieNode()
                curr = curr.children[let]
            curr.word = word
        
        # go through coords
        acc = []
        visited = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root.children:
                    dfs(root, set(), i, j)
        
        return acc

class TrieNode:
    def __init__(self):
        self.word = None
        self.found = False
        self.children = {} # map let to TrieNode
