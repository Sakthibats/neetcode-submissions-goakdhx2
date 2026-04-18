class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b!=0:
            carry = (a&b) << 1
            # print(a, b, carry)
            # print(bin(a), bin(b), bin(carry))
            a = (a^b) & mask
            b = carry & mask
            # print("----")
            # print(a, b, carry)
            # print(bin(a), bin(b), bin(carry))
        return a if  a <= max_int else ~(a^mask)



        