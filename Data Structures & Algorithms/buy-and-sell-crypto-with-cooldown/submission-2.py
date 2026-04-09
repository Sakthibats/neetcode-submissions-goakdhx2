class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def help(profit, prevsold, ind):
            if ind>=len(prices):
                return profit
            # elif ind in memo:
            #     return memo[ind]
            else:
                ans = 0
                if prevsold: #need to buy
                    ans = max(
                        help(profit - prices[ind], False,ind+1),
                        help(profit, True, ind+1)
                        )
                else: #need to sell
                    ans = max(
                        help(profit+prices[ind], True, ind+2), 
                        help(profit,False, ind+1)
                        )
                memo[ind] = ans
                return ans
        return max(0, help(0, True, 0))
        