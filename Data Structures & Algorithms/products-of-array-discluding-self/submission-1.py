class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forw = [1]
        back = [1]
        for i in range(len(nums)):
            forw.append(forw[-1]*nums[i])
            back.append(back[-1]*nums[-1-i])
        back = back[1:][::-1]
        forw = forw[1:]
        # print(forw, back)
        fin = []
        for i in range(len(nums)):
            if i==0:
                fin.append(back[1])
            elif i==(len(nums)-1):
                fin.append(forw[-2])
            else:
                fin.append(forw[i-1]*back[i+1])
        return fin
                


        