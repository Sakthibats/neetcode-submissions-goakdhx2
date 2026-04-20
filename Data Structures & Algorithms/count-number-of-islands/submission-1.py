class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        count = 0

        def help(i, j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]=="0":
                return
            if grid[i][j] == "1":
                grid[i][j] = "0"
                for l, r in direction:
                    help(i+l, j+r)
                return
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                item = grid[i][j]
                if item == "1":
                    count +=1
                    help(i, j)
        return count

                    

        