class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic= {}
        for ind, item in enumerate(nums):
            if target-item in dic:
                return [dic[target-item], ind]
            else:
                dic[item] = ind
        
                
        