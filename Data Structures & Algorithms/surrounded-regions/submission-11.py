from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        # try 2: flood edges, fill remaining
        def dfs(i, j):
            if board[i][j] != 'O':
                return
            board[i][j] = '_'
            if i > 0 and board[i-1][j] == 'O':
                dfs(i-1, j)
            if j > 0 and board[i][j-1] == 'O':
                dfs(i, j-1)
            if i < len(board)-1 and board[i+1][j] == 'O':
                dfs(i+1, j)
            if j < len(board[0])-1 and board[i][j+1] == 'O':
                dfs(i, j+1)
                
        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0])-1)
        for j in range(len(board[0])):
            dfs(0, j)
            dfs(len(board)-1, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '_':
                    board[i][j] = 'O'

        return 

        # try 1: search for surrounded and fill
        def surrounded(i, j):
            visited = set()
            q = deque([(i, j)])
            
            while q:
                i, j = q.popleft()
                if (i, j) in visited:
                    continue
                if i == 0 or j == 0 or i == len(board)-1 or j == len(board[0])-1:
                    return False
                visited.add((i, j))

                if i > 0 and board[i-1][j] == 'O':
                    q.append((i-1, j))
                if j > 0 and board[i][j-1] == 'O':
                    q.append((i, j-1))
                if i < len(board)-1 and board[i+1][j] == 'O':
                    q.append((i+1, j))
                if j < len(board[0])-1 and board[i][j+1] == 'O':
                    q.append((i, j+1))
                  
            return True

        def fill(i, j):
            visited = set()
            q = deque([(i, j)])
            
            while q:
                i, j = q.popleft()
                if (i, j) in visited:
                    continue
                if i == 0 or j == 0 or i == len(board)-1 or j == len(board[0])-1:
                    return False
                visited.add((i, j))
                board[i][j] = 'X'

                if i > 0 and board[i-1][j] == 'O':
                    q.append((i-1, j))
                if j > 0 and board[i][j-1] == 'O':
                    q.append((i, j-1))
                if i < len(board)-1 and board[i+1][j] == 'O':
                    q.append((i+1, j))
                if j < len(board[0])-1 and board[i][j+1] == 'O':
                    q.append((i, j+1))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    continue
                if surrounded(i, j):
                    fill(i, j)
                
                