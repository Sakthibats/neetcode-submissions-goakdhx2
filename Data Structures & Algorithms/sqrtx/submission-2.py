class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0 
        left, right = 1, x
        while (right-left)>1:
            mid = (left+right)//2
            if mid*mid>x:
                right= mid
            else:
                left = mid
        return left