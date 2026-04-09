class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [-i for i in stones]
        heapq.heapify(arr)

        while len(arr)>1:
            largest = heapq.heappop(arr)*-1
            nextLarge = heapq.heappop(arr)*-1
            if largest-nextLarge>0:
                heapq.heappush(arr, -(largest-nextLarge))
        if arr:
            return arr[0]*-1
        return 0