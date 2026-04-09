class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        start = 0
        summ = 0
        for i in range(len(gas)):
            net = gas[i]- cost[i]
            total+=net
            summ+= net
            if total<0:
                total = 0
                start = i+1

        if summ<0:
            return -1
        return start