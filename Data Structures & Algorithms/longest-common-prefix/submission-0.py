class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string = ""

        for i in range(len(strs[0])):
            char = strs[0][i]
            for word in strs[1:]:
                if i >= len(word) or char != word[i]:
                    return string
            string += char
            print(string)
        return string


        