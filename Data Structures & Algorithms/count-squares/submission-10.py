from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.x_y = defaultdict(lambda: defaultdict(int)) # x:{y:count}

    def add(self, point: List[int]) -> None:
        x, y = point
        self.x_y[x][y] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point
        for y_cand in self.x_y[x]:
            if y_cand == y:
                continue
            dist = abs(y-y_cand)
            # check if other point exists (x-dist, y) or (x+dist, y)
            # (x, y), (x, y_cand), (x-dist, y), (x-dist, y_cand)
            n, p = x-dist, x+dist
            p1 = n in self.x_y and y in self.x_y[n] and y_cand in self.x_y[n]
            p2 = p in self.x_y and y in self.x_y[p] and y_cand in self.x_y[p]

            if p1:
                b = self.x_y[x][y_cand]
                c = self.x_y[n][y]
                d = self.x_y[n][y_cand]
                res += b*c*d
            if p2:
                b = self.x_y[x][y_cand]
                c = self.x_y[p][y]
                d = self.x_y[p][y_cand]
                res += b*c*d
        return res