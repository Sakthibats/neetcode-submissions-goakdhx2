class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def testing(piles, k):
            count = 0
            for i in piles:
                count += math.ceil(i/k)
            return count

        minn, maxx = 1, max(piles)
        med = maxx
        while minn<=maxx:
            med = (minn+maxx)//2
            count = testing(piles, med)
            if count>h:
                minn = med+1
            else:
                maxx = med-1
        return minn



        
        