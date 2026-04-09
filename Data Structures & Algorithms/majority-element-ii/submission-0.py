class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = len(nums)//3
        heap = []
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
        heap = []
        for key, val in dic.items():
            heapq.heappush(heap, (-val, key))
        
        # item = heapq.heappop(heap)
        fin = []
        # print(heap[0])
        # print(heap)
        # print(heap[0][0], target)
        while heap and (-heap[0][0])>target:
            fin.append(heap[0][1])
            heapq.heappop(heap)
        return fin
