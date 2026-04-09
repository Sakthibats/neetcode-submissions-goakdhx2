class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        h = []
        for item, count in dic.items():
            heapq.heappush(h, (-count, item))
        # print(h)
        arr = []
        for i in range(k):
            target = heapq.heappop(h)
            arr.append(target[1])
        return arr


        