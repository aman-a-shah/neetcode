from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # find rotten fruits into q
        q = deque()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    count += 1
        
        time = 0

        # bfs with multi-start q
        while q and count > 0:
            for _ in range(len(q)):
                i, j = q.popleft()
                
                if i > 0 and grid[i-1][j] == 1:
                    q.append((i-1, j))
                    grid[i-1][j] = 2
                    count -= 1
                if j > 0 and grid[i][j-1] == 1:
                    q.append((i, j-1))
                    grid[i][j-1] = 2
                    count -= 1
                if i < len(grid)-1 and grid[i+1][j] == 1:
                    q.append((i+1, j))
                    grid[i+1][j] = 2
                    count -= 1
                if j < len(grid[0])-1 and grid[i][j+1] == 1:
                    q.append((i, j+1)) 
                    grid[i][j+1] = 2
                    count -= 1
            time += 1

        return time if count <= 0 else -1