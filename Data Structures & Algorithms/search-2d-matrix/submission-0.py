class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cur_row = 0
        cur_col = 0

        while matrix[cur_row][-1] < target:
            cur_row += 1
            if cur_row >= len(matrix):
                return False
        
        for i in range(len(matrix[0])):
            if matrix[cur_row][i] == target:
                return True
        
        return False