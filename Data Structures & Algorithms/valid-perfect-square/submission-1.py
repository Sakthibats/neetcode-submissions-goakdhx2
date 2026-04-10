class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r  = 1, num
        while l<=r:
            m = l+(r-l)//2
            print(l, r, m)
            msq = m*m
            if msq<num:
                l = m+1
            elif msq==num:
                return True
            else:
                r = m-1
        return False
            
        