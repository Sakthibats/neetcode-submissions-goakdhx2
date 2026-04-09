class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        fin = {}
        for i in strs:
            sortt = "".join(sorted(i))
            fin[sortt] = fin.get(sortt, []) + [i]
        return list(fin.values())


        