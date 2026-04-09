class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            item = nums[i]
            if target-item in dic:
                return [dic[target-item], i]
            else:
                dic[item] = i
        