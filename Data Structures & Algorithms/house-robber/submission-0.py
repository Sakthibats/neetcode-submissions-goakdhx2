class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def help(ind):
            nonlocal memo
            if ind>=(len(nums)):
                return 0
            elif ind in memo:
                return memo[ind]
            else:
                ans = max(help(ind+1), nums[ind]+help(ind+2))
                memo[ind] = ans
                return ans
        answer =  help(0)
        # print(memo)
        return answer

        