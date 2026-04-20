class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dir = [(1,0), (-1,0), (0, 1), (0, -1)]

        def help(i, j):
            if i<0 or i >=len(grid) or j <0 or j>=len(grid[0]) or grid[i][j]==0:
                return 0
            else:
                # print(i, j)
                cnt = 0
                grid[i][j] = 0
                for l, r in dir:
                    cnt += help(i+l, j+r)
                # print(cnt)
                return 1 + cnt
        maxx = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count = help(i, j)
                    maxx = max(maxx, count)
        return maxx

