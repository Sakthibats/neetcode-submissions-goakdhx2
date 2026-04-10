import heapq

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        ngifts = [-i for i in gifts]
        heapq.heapify(ngifts)

        for i in range(k):
            n = -heapq.heappop(ngifts)
            heapq.heappush(ngifts, -floor(sqrt(n)))
            # print(ngifts)
        return -sum(ngifts)


        