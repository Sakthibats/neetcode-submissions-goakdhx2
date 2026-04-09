class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        listt = sorted(list(count.items()), key=lambda x: x[1])
        arr = []
        for i in range(k):
            item = listt.pop()[0]
            arr.append(item)
        return arr


        
        