from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # bfs from edges
        def bfs(q):
            visited = deque()
            while q:
                i, j = q.popleft()
                if [i, j] in visited:
                    continue
                visited.append([i, j])

                if i > 0 and heights[i-1][j] >= heights[i][j]:
                    q.append([i-1, j])
                if j > 0 and heights[i][j-1] >= heights[i][j]:
                    q.append([i, j-1])
                if i < len(heights)-1 and heights[i+1][j] >= heights[i][j]:
                    q.append([i+1, j])
                if j < len(heights[0])-1 and heights[i][j+1] >= heights[i][j]:
                    q.append([i, j+1])

            return visited

        # create queues
        q_pac = deque()
        q_atl = deque()

        for i in range(len(heights)):
            q_pac.append((i, 0))
            q_atl.append((i, len(heights[0])-1))
        for j in range(len(heights[0])):
            q_pac.append((0, j))
            q_atl.append((len(heights)-1, j))
       
        # find intersection
        pac = bfs(q_pac)
        atl = bfs(q_atl)

        return [coord for coord in pac if coord in atl]