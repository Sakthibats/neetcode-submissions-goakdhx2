class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #subbox
        dic = {}
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col]== ".":
                    continue
                subbox_row = row//3
                subbox_col = col//3
                if board[row][col] in dic.get((subbox_row, subbox_col), []):
                    return False
                else:
                    dic[(subbox_row, subbox_col)] = dic.get((subbox_row, subbox_col), []) + [board[row][col]]
        # print(dic)
        #check rows
        for row in board:
            new_row = list(filter(lambda x: x!=".", row))
            # print("row", new_row)
            if len(set(new_row))!=len(new_row):
                return False
        
        for col in range(len(board[0])):
            arr = []
            for row in range(len(board)):
                if board[row][col]!=".":
                    if board[row][col] in arr:
                        return False
                    else:
                        arr.append(board[row][col])
                # print(arr)
        
        return True



                    