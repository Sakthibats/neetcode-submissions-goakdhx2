class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        for ind, item in enumerate(nums2):
            dic[item] = ind
        fin = []
        for i in nums1:
            fin.append(dic[i])
        return fin