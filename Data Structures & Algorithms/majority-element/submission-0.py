class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        threshold = len(nums) // 2
        print(threshold)

        for num in nums:
            count[num] = count.get(num, 0) + 1
            print(count)
            if count[num] > threshold:
                return num
        