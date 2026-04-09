class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newarr = []
        dic = {}
        for i in range(len(strs)):
            item = "".join(sorted(strs[i]))
            newarr.append(item)
            dic[item] = dic.get(item, []) + [strs[i]]
        # print(newarr)
        # print(dic)
        return list(dic.values())

        newstr = sorted(strs)