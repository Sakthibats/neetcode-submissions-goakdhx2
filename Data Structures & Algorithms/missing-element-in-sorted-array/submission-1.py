class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums)-1
        while l<r:
            mid = r-(r-l)//2
            ln, mn, rn = nums[l],  nums[mid],  nums[r]
            if (nums[mid]-nums[0])-mid <k:
                l = mid
            else:
                r = mid-1
        return nums[0] + k + l
        