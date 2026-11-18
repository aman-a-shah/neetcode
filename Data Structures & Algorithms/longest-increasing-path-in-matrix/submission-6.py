class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        # dp[i][j] = max increasing path from (i, j)
        dp = {} # (i, j):longest path

        res = 0

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            path = 0
            if i > 0 and matrix[i-1][j] > matrix[i][j]:
                path = max(path, dfs(i-1, j))
            if j > 0 and matrix[i][j-1] > matrix[i][j]:
                path = max(path, dfs(i, j-1))
            if i < len(matrix)-1 and matrix[i+1][j] > matrix[i][j]:
                path = max(path, dfs(i+1, j))
            if j < len(matrix[0])-1 and matrix[i][j+1] > matrix[i][j]:
                path = max(path, dfs(i, j+1))

            path += 1
            dp[(i, j)] = path
            return path 

        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))

        return res