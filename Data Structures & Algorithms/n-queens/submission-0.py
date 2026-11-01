class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols, d1, d2 = set(), set(), set()
        placement = []                     # placement[r] = col of queen in row r

        def backtrack(r):
            if r == n:                     # goal: all rows filled
                res.append(["".join("Q" if c == placement[i] else "."
                                    for c in range(n)) for i in range(n)])
                return
            for c in range(n):             # choices: columns in this row
                if c in cols or (r - c) in d1 or (r + c) in d2:
                    continue               # constraint: attacked
                cols.add(c); d1.add(r - c); d2.add(r + c)   # place
                placement.append(c)
                backtrack(r + 1)           # recurse
                placement.pop()            # undo
                cols.remove(c); d1.remove(r - c); d2.remove(r + c)

        backtrack(0)
        return res