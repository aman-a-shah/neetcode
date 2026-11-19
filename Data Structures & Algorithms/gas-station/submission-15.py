class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        start = 0
        tot_gas = gas[0]
        
        for i in range(1, len(gas)):
            tot_gas -= cost[i-1]

            if tot_gas < 0:
                start = i
                tot_gas = 0
            tot_gas += gas[i]
            
        return start