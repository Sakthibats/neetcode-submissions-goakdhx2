class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum = {0:1}
        count = 0
        fin = 0
        for i, j in enumerate(nums):
            count +=j
            fin += prefixsum.get(count-k, 0)
            prefixsum[count] = prefixsum.get(count, 0) + 1

        print(prefixsum)
        return fin

