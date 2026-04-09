class Solution:
    def canJump(self, nums: List[int]) -> bool:
        fuel = nums[0]
        curr = 0
        while fuel<len(nums) and curr<len(nums):
            fuel = max(curr + nums[curr], fuel)
            print(fuel, curr)
            if curr==fuel and fuel<(len(nums)-1):
                return False
            else:
                curr+=1
        return True
            