class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        offset = 0
        m, n = len(matrix), len(matrix[0])
        res = []
        
        while offset < (min(m, n)+1)//2:
            # top
            for i in range(offset, n-offset):
                res.append(matrix[offset][i])
            # right
            for i in range(offset+1, m-offset):
                res.append(matrix[i][n-offset-1])
            # bottom 
            if m-offset-1 != offset:
                for i in range(n-offset-2, offset-1, -1):
                    res.append(matrix[m-offset-1][i])
            # left
            if n-offset-1 != offset:
                for i in range(m-offset-2, offset, -1):
                    res.append(matrix[i][offset])

            offset += 1

        return res

        # # # #
        # # # #
        # # # #