class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        fir, sec, thir = arr[0], arr[1], arr[2]
        diff = min(abs(sec-fir), abs(thir-sec))
        if fir>sec:
            diff  *= -1
        if diff == 0:
            return fir
        start = fir
        for i in range(len(arr)):
            if ((start+diff*i)==arr[i]):
                pass
            else:
                return (start+diff*i)
