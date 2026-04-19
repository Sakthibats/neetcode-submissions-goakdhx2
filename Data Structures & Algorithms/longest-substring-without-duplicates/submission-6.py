class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        start = 0
        maxx = 0
        for ind, item in enumerate(s):
            if item in dic:
                maxx = max(maxx, ind-start)
                start = max(start, dic[item]+1)
                dic[item] = ind
            elif ind == (len(s)-1):
                maxx = max(maxx, ind-start+1)
            else:
                dic[item] = ind
        return maxx

        
