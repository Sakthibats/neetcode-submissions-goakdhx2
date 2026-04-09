class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        arr = sorted(nums, reverse=True)
        print(arr)
        for i in range(1, len(nums)):
            prev, curr = arr[i-1], arr[i]
            print(prev, curr)
            if prev!=curr and prev!=-1:
                return prev
            if prev==curr:
                arr[i]=-1
                arr[i-1]=-1
        return arr[-1]
            