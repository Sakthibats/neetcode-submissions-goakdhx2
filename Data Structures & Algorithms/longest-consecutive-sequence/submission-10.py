class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        nums.sort()
        running = nums[0]
        max_count = 1
        count = 1
        print(nums)
        for i in range(1, len(nums)):
            if (nums[i]-1)==running:
                count+=1
                max_count = max(max_count, count)
            elif nums[i]==running:
                pass
            else:
                count = 1
            running = nums[i]
        return max_count
        
        