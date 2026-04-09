class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if (len(hand)%groupSize)>0:
            return False
        dic = {}

        for i in hand:
            dic[i] = dic.get(i, 0) + 1
        
        keys = sorted(list(dic.keys()))
        pitem = 0
        while pitem<len(keys):
            if dic[keys[pitem]]==0:
                pitem+=1
            else:
                fill = 0
                item = keys[pitem]
                print(item)
                while fill<groupSize:
                    print("whileloop", fill, item)
                    if dic.get(item, 0)>0:
                        dic[item]-=1
                        fill+=1
                        item+=1
                    else:
                        return False
                if dic[keys[pitem]]==0:
                    pitem+=1
        return True

                    

