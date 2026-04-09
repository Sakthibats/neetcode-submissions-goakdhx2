class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize>0:
            return False

        dic = {}
        for i in hand:
            dic[i] = dic.get(i, 0) + 1
        
        arr = sorted(list(dic.keys()))
        stind = 0
        count = 0
        while count < len(hand):
            start = arr[stind]
            if dic[start]<=0:
                stind+=1
            else:
                for i in range(start, start+groupSize):
                    if dic.get(i, 0)<=0:
                        return False
                    else:
                        dic[i] -=1
                        count+=1

        return True
