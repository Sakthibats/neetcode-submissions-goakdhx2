class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        hor = set()
        vert = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                item = matrix[i][j]
                if item == 0:
                    hor.add(i)
                    vert.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in hor:
                    matrix[i][j] = 0
                if j in vert:
                    matrix[i][j] = 0


                
        