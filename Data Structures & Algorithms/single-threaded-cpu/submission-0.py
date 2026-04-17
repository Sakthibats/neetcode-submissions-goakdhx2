class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        avail = []
        pend = []
        for i, (enq, process) in enumerate(tasks):
            heapq.heappush(pend, (enq, process, i))
        time =0 
        res = []
        while pend or avail:
            while pend and pend[0][0] <= time:
                enqtime, processtime, i = heapq.heappop(pend)
                heapq.heappush(avail, (processtime, i ))
            if not avail:
                time = pend[0][0]
                continue
            processtime, i = heapq.heappop(avail)
            time += processtime
            res.append(i)
        return res

