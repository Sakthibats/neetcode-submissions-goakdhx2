class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            print(key)
            dic[key].append(word)
            print(dic)
        return list(dic.values())