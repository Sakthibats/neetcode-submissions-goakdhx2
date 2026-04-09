class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        col = len(matrix[0])
        top, bot = 0, rows-1
        while top <= bot:
            mid_row = (top+bot)//2
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot = mid_row - 1
            else:
                break
        if not (top <= bot):
            return False
        mid_row = (top+bot)//2
        l, r = 0, col - 1
        while l <= r:
            m = (l+r)//2
            if target > matrix[mid_row][m]:
                l = m + 1
            elif target < matrix[mid_row][m]:
                r = m - 1
            else:
                return True
        return False
        
