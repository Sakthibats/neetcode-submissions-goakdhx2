class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def help(pos):
            if pos in memo:
                return memo[pos]
            if pos==(len(nums)-1):
                return 0
            if nums[pos] == 0:
                return 10000000000
            
            end = min(len(nums), pos+nums[pos]+1)
            res = math.inf
            for j in range(pos+1, end):
                res = min(res, 1+help(j))
            memo[pos] =  res
            return res
        return help(0)
        