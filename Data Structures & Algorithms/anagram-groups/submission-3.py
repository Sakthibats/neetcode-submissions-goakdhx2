class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for word in strs:
            tup = self.tuplify(word)
            dic[tup] = dic.get(tup, [])+ [word]
        return list(dic.values())

    def tuplify(self, string):
        count = [0]*26
        for i in string:
            count[ord(i)-ord('a')] +=1
        return tuple(count)
