class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        def help(t1, t2):
            return [max(t1[0], t2[0]),max(t1[1], t2[1]),max(t1[2], t2[2])]

        fir, sec, thi = [], [], []
        good=set()
        for i in range(len(triplets)):
            trip = triplets[i]
            f1, f2, f3 = trip
            if f1>target[0] or f2>target[1] or f3>target[2]:
                continue
            elif f1==target[0]:
                fir.append(i)
                good.add(0)
            if f2==target[1]:
                sec.append(i)
                good.add(1)
            if f3==target[2]:
                thi.append(i)
                good.add(2)


        return len(good)==3
