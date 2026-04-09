class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        curr = 0
        maxlen = 0
        for i in range(len(s)):
            item = s[i]
            if item in dic:
                curr = max(curr, dic[item]+1)            
            dic[item] = i
            maxlen = max(maxlen, i-curr+1)
        return maxlen
        