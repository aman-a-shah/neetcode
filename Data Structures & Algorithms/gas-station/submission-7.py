class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        start = 0
        tot_gas = 0
        for i in range(len(gas)):
            tot_gas += gas[i]-cost[i]
            if tot_gas < 0:
                start = i+1
                tot_gas = 0
        return start