class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        order = []
        for i in range(len(s)):
            item = s[i]
            if item not in dic:
                dic[item] = [i, i]
                order.append(item)
            else:
                dic[item][1] = i
        intervals = list(dic.values())
        # print(intervals)
        fin = [intervals[0]]
        for i in range(1, len(intervals)):
            lastfin = fin.pop()
            curr = intervals[i]
            if lastfin[1]>curr[0]:
                lastfin = [lastfin[0], max(lastfin[1], curr[1])]
                fin.append(lastfin)
            else:
                fin.append(lastfin)
                fin.append(curr)
        # print(fin)
        finale = [j-i+1 for i, j in fin]
        # print(finale)
        return finale
        