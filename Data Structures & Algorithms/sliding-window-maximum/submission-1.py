class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        fin = []
        for i in range(k):
            heapq.heappush(heap, -nums[i])
        
        fin.append(-heap[0])
        for i in range(len(nums)-k):
            start = nums[i]
            end = nums[k+i]
            heap.remove(-start)
            heapq.heapify(heap)
            heapq.heappush(heap, -end)
            fin.append(-heap[0])
            # print(heap)
        return fin



        

        