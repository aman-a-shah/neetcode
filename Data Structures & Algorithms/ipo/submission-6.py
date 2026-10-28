import heapq

class Solution:
    def findMaximizedCapital(self, k, w, profits: List[int], capital: List[int]):
        # for each of the k projects, want to pick greatest profit for capital
        cur_cap = w
        available_profits = []

        # map cap to i sorted
        cap_i = []
        for i, cap in enumerate(capital):
            cap_i.append([cap, i])
        heapq.heapify(cap_i) # order cap increasing, with i

        for i in range(k):
            # get all profits into 
            while cap_i and cap_i[0][0] <= cur_cap:
                profit = profits[heapq.heappop(cap_i)[1]]
                heapq.heappush(available_profits, -profit)
            
            # pick largest and continue
            if available_profits:
                max_profit = heapq.heappop(available_profits)
                cur_cap += -max_profit

        return cur_cap