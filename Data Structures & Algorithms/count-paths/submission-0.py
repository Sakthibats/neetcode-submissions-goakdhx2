class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def help(i, j):
            if i==m and j==n:
                return 1
            if i>m or j>n:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            else:
                ans = help(i+1, j) + help(i, j+1)
                memo[(i, j)] = ans
                return ans
        fin = help(1, 1)
        return fin

        