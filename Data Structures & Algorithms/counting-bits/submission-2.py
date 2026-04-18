class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        dic = {}
        for i in range(n+1):
            item = i
            count = 0
            while item:
                if item in dic:
                    count += dic[item]
                    item =0
                else:
                    if item &1:
                        count +=1
                    item >>=1
            dic[i] = count
            res.append(count)
        return res
        

        