class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def help(i, j):
            if i==len(word1):
                return abs(len(word2)-j)
            if j==len(word2):
                return abs(len(word1)-i)
            else:
                if word1[i]==word2[j]:
                    memo[(i, j)] = help(i+1, j+1)
                elif (i, j) in memo:
                    return memo[(i, j)]
                else:
                    memo[(i, j)] = 1 + min(help(i,j+1), help(i+1, j), help(i+1, j+1))
                return memo[(i, j)]
        return help(0, 0)

    
        