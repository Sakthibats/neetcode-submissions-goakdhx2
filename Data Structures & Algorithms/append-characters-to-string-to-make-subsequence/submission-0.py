class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        tind = 0 
        for i in range(len(s)):
            if s[i] == t[tind]:
                tind += 1
                if tind==len(t):
                    return 0
            
        return len(t)-tind

        