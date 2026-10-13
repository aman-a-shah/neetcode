class StockSpanner:

    acc: list

    def __init__(self):
        self.acc = []

    def next(self, price: int) -> int:
        ans = 0

        self.acc.append(price)
        for i in range(len(self.acc)-1, -1, -1):
            if self.acc[i] <= price:
                ans += 1
            else:
                break

        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)