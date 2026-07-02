class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                list_1 = []                          
                for i in range(3):
                    for j in range(3):
                        if board[r+i][c+j] == '.':
                            continue                  
                        else:
                            list_1.append(board[r+i][c+j])
                if len(list_1) != len(set(list_1)):
                    return False

        for i in range(9):
            list_3 = []
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    list_3.append(board[i][j])
                    if len(list_3) != len(set(list_3)):
                        return False
        
        for i in range(9):
            list_2 = []
            for j in range(9):
                if board[j][i] == '.':
                    continue
                else:
                    list_2.append(board[j][i])
                    if len(list_2) != len(set(list_2)):
                        return False

        return True