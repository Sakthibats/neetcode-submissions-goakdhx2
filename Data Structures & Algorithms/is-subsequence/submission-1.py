class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sind = 0
        if len(s)==0:
            return True
        for i in range(len(t)):
            if s[sind]==t[i]:
                sind+=1
                if sind==len(s):
                    return True
        return False
    
        