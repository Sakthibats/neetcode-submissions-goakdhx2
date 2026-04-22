class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        nums = sorted(people)
        res  = 0

        l, r = 0, len(nums)-1

        while l<=r:
            remain = limit-nums[r]
            r-=1
            res +=1
            if l<=r and remain >= nums[l]:
                l+=1
        return res
            
           
