class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        indnum = [(num, ind) for ind, num in enumerate(nums)]
        heapq.heapify(indnum)
        for _ in range(k):
            item, index = heapq.heappop(indnum)
            nums[index] *= multiplier
            heapq.heappush(indnum, (item*multiplier, index))
            # print(indnum)
        return nums