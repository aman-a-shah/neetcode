class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        acc = [[0] * len(matrix) for _ in matrix[0]]

        for col in range(len(matrix)): 
            for row in range(len(matrix[0])):
                acc[row][col] = matrix[col][row]

        return acc