class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            print(f"Value we are checking is {val}")
            print(f"Current number is {nums[i]}")
            if val != nums[i]:
                nums[k] = nums[i]
                k += 1
                print(f"Value of k is {k}")
        return k
