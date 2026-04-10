class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dic = {}
        for id, score in items:
            dic[id] = dic.get(id, [])+[-score]
        findic = {}
        for i in dic.keys():
            arr = dic[i]
            heapq.heapify(arr)
            summ = 0
            for j in range(5):
                value = heapq.heappop(arr)
                summ+=value
            findic[i] = -summ//5
        result = sorted([[k, v] for k, v in findic.items()], key=lambda x: x[0])
        return result

        