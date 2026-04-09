class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l<r:
            if s[l]!=s[r]:
                leftpop = s[l+1:r+1]
                rightpop = s[l:r]
                return leftpop==leftpop[::-1] or rightpop==rightpop[::-1]
            l, r = l+1, r-1
        return True
        