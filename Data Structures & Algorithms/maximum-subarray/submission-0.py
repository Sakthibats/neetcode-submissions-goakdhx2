class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = nums[0]
        currsum = nums[0]

        for i in range(1, len(nums)):
            currsum = max(currsum+nums[i], nums[i])
            maxx = max(maxx, currsum)
        return maxx

