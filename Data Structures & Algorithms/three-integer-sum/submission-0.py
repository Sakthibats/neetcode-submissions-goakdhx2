class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        fin = set()
        for ind, item in enumerate(nums):
            target = -item
            dic = {}
            for ind_n, item_new in enumerate(nums[ind+1:]):
                if target-item_new in dic:
                    fin.add(tuple(sorted([item, target-item_new, item_new])))
                else:
                    dic[item_new] = ind_n
        return [list(i) for i in fin]
        