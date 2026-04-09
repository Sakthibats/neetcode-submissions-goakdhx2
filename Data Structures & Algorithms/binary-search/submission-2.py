class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left<right:
            m = left + ((right-left)//2)
            if nums[m] >=target:
                right = m
            elif nums[m] < target:
                left = m+1
        if (left<len(nums) and nums[left]==target):
            return left 
        else:
            return -1    