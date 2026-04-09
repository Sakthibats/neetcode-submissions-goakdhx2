class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.strip().split(" ")[-1]
        return len(string)
        