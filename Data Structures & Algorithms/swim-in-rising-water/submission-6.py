import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [] # time, i, j
        heapq.heappush(heap, (grid[0][0],0,0))
        visited = set()
        min_time = 0

        while heap:
            time, i, j = heapq.heappop(heap)
            min_time = max(min_time, time)
            if (i, j) == (len(grid)-1, len(grid[0])-1):
                return min_time
            if (i, j) in visited:
                continue
            visited.add((i, j))

            if i > 0:
                heapq.heappush(heap, (max(time, grid[i-1][j]), i-1, j))
            if j > 0:
                heapq.heappush(heap, (max(time, grid[i][j-1]), i, j-1))
            if i < len(grid)-1:
                heapq.heappush(heap, (max(time, grid[i+1][j]), i+1, j))
            if j < len(grid[0])-1:
                heapq.heappush(heap, (max(time, grid[i][j+1]), i, j+1))

        return -1
        