class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        maxx = 0
        count = 0

        def dfs(r, c):
            nonlocal count
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]==0:
                return 
            count+=1
            grid[r][c] = 0
            for dr, dc in directions:
                dfs(dr+r, dc+c)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print(i, j, grid[i][j])
                if grid[i][j] == 1:
                    dfs(i, j)
                    # print(maxx, count )
                    maxx = max(maxx, count)
                    count = 0
        return maxx
        