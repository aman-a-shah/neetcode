class StockSpanner:

    acc: list

    def __init__(self):
        self.acc = []

    def next(self, price: int) -> int:
        ans = 1

        while self.acc and self.acc[-1][0] <= price:
            ans += self.acc.pop(-1)[1]
        self.acc.append((price, ans))
        
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)