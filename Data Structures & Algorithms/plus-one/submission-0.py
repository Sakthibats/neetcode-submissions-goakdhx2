class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = digits[::-1]
        carry = 0
        for ind, item in enumerate(nums):
            if ind==0:
                summ = nums[ind]+1+carry
            else:
                summ = nums[ind] + carry
            if summ>9:
                nums[ind] = 0
                carry = 1
            else:
                nums[ind] = summ
                carry = 0
        if carry==1:
            nums.append(1)
        return nums[::-1]

        