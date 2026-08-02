class NumMatrix:

    matrix: List[List[int]]

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        acc = 0

        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                acc += self.matrix[i][j]

        return acc


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)