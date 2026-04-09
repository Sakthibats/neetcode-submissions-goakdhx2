class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        print(f'Init l at {l}, and r at {r}')
        res = 0

        while l <= r:
            m = l + (r - l) // 2
            #print(f'Init m at {m}')
            if m*m > x:
                r = m - 1
                #print(f'Now r is moved to {r}')
            elif m*m < x:
                l = m + 1
                #print(f'Now l is moved to {l}')
                res = m
                #print(f'Current result is {res}')
            else:
                return m
        return res



        