class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums)-1
        summ = nums[start] + nums[end]
        while summ!=target:
            if summ>target:
                end-=1
            else:
                start+=1
            summ = nums[start] + nums[end]
        return [start+1, end+1]
        