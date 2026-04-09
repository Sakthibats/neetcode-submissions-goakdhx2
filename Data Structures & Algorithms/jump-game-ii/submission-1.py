class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def help(i):
            if i in memo:
                return memo[i]
            if i==len(nums)-1:
                return 0
            if nums[i] == 0:
                return 100000
            
            res = 100000
            end = min(len(nums), i+nums[i] +1)
            for j in range(i+1, end):
                res = min(res, 1+help(j))
            memo[i] = res
            return res
        return help(0)
        

        