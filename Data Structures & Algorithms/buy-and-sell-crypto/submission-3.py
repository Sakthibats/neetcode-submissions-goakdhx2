class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = prices[0]
        profit = 0
        for i in prices:
            profit = max(profit, i-minn)
            minn = min(minn, i)
        return profit

        