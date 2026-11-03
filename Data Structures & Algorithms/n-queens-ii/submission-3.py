class Solution:
    def totalNQueens(self, n: int) -> int:
        
        acc = 0
        straight = set()
        diag1 = set()
        diag2 = set()

        def dfs(n_queens, row):
            nonlocal acc

            if n_queens == n:
                acc += 1
                return
            if row >= n:
                return

            for col in range(n):
                # check valid
                if col in straight or (col-row) in diag1 or (col+row) in diag2:
                    continue
                
                # update straight + diag
                straight.add(col)
                diag1.add(col-row)
                diag2.add(col+row)
                # recurse
                dfs(n_queens + 1, row + 1)
                # revert straight + diag
                straight.remove(col)
                diag1.remove(col-row)
                diag2.remove(col+row)

        dfs(0, 0)
        return acc