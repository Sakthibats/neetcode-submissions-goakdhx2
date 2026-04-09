class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def help(pos):
            if pos>=len(nums):
                return 0
            elif pos in memo:
                return memo[pos]
            else:
                ans = max(help(pos+1), nums[pos]+help(pos+2))
                memo[pos] = ans
                return ans
        return help(0)


        