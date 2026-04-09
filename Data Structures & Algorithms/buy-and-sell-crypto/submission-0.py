class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        maxx = 0
        for i in prices[1:]:
            maxx = max(maxx, i-lowest)
            lowest = min(lowest, i)
        return maxx
        