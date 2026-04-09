class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxx = nums[0]
        for i in range(len(nums)):
            item = nums[i]
            if maxx<i:
                return False
            maxx = max(maxx, i+item)
            if maxx>=(len(nums)-1):
                return True
        return False


            