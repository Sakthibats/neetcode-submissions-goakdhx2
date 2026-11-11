class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ss, tt = sorted(s), sorted(t)
        return ss==tt

        