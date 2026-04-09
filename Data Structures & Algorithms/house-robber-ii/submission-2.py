class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def help(ind, num):
            if ind>=len(num):
                return 0
            if ind in memo:
                return memo[ind]
            else:
                ans = max(help(ind+1, num), num[ind] + help(ind+2, num))
                memo[ind] = ans
                return ans

        memo={}
        fir = help(0, nums[1:])
        memo={}
        sec = help(0, nums[:-1])
        return max(fir, sec)