class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forwardstart = 1
        forw = []
        backwardstart = 1
        back = []
        for i in range(len(nums)):
            forwardstart = forwardstart*nums[i]
            forw.append(forwardstart)
            backwardstart = backwardstart*nums[-i-1]
            back.append(backwardstart)
        back = back[::-1]
        # print(forw, back)
        res = []
        for i in range(len(nums)):
            if i==0:
                res.append(back[i+1])
            elif i==(len(nums)-1):
                res.append(forw[i-1])
            else:
                res.append(forw[i-1]*back[i+1])
        return res




