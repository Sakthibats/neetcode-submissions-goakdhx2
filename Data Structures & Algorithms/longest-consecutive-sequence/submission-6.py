class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums:
            arr = sorted(list(set(nums)))
            # print(arr)
            prev = arr[0]
            maxx = 1
            count = 1
            for item in arr[1:]:
                # print(item, prev, maxx, count)
                if item<=(prev+1):
                    count+=1
                    maxx = max(maxx, count)
                else:
                    count=1
                prev = item

            return maxx
        return 0

        