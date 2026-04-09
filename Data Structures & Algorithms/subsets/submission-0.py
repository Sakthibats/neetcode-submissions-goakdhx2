class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        fin = []
        def helper(remain, curr):
            nonlocal fin
            fin.append(curr)
            for i in range(len(remain)):
                helper(remain[i+1:], curr+[remain[i]])
        helper(nums, [])
        return fin
        