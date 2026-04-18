class Solution:
    def hammingWeight(self, num: int) -> int:
        count = 0
        while num:
            if num&1:
                count +=1
            num = num >> 1
        return count


        