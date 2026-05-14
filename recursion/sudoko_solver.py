# +-------+-------+-------+
# | 5 3 . | . 7 . | . . . |
# | 6 . . | 1 9 5 | . . . |
# | . 9 8 | . . . | . 6 . |
# +-------+-------+-------+
# | 8 . . | . 6 . | . . 3 |
# | 4 . . | 8 . 3 | . . 1 |
# | 7 . . | . 2 . | . . 6 |
# +-------+-------+-------+
# | . 6 . | . . . | 2 8 . |
# | . . . | 4 1 9 | . . 5 |
# | . . . | . 8 . | . 7 9 |
# +-------+-------+-------+

# Conditions:
  # Each of the digits 1-9 must occur exactly once in each row.
  # Each of the digits 1-9 must occur exactly once in each column.
  # Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

def isSafe(board,row,col,count):
    for value in range(9):
        if board[row][value]==str(count):
            return False
        if board[value][col]==str(count):
            return False
        if board[3*(row//3)+value//3][3*(col//3)+value%3]==str(count):
            return False
    return True
    
        
def sudoku(board,i,j,ans):
    if i>=8 and j>=8:
        print(board)
        return True
    
    for row in range(i,9):
        for col in range(j,9):
            if board[row][col]=='.':     
                for count in range(1,10):
                    if isSafe(board,row,col,count):
                        board[row][col]=str(count)
                        if sudoku(board,row,col,ans)==True:
                            return True
                        board[row][col]='.'
          
          
ans=[]
print(sudoku(board,0,0,ans))
print(ans)
