class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0

        def dfs(i, j):
            if (i, j) in visited or i < 0 or j < 0:
                return 0
            if i >= len(grid) or j >= len(grid[0]):
                return 0
            if grid[i][j] == 0:
                return 0
            
            visited.add((i, j))

            up = dfs(i-1, j)
            down = dfs(i+1, j)
            left = dfs(i, j-1)
            right = dfs(i, j+1)

            return 1 + up + down + left + right

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visited or grid[i][j] == 0:
                    continue
                max_area = max(max_area, dfs(i, j))

        return max_area