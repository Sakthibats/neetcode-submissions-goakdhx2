class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = [(math.sqrt(pt[0]**2+pt[1]**2), ind)for ind, pt in enumerate(points)]
        heapq.heapify(arr)
        fin = []
        for i in range(k):
            index = heapq.heappop(arr)[1]
            fin.append(points[index])
        return fin
