class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for num in nums:
            ids = abs(num)-1
            if nums[ids]<0:
                return abs(num)
            nums[ids] *= -1
            print(num, nums)
        return -1
        