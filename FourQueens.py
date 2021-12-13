# Check if there is a solution to the problem
# Brute force O(4^4) time
# 1. No queens on the same column
# 2. No queens on the same rows
# 3. No queens on the same diagonal

def fourQueens(board, n):
    for i in range(n):
        # print(2)
        board[i][0] = 1
        for j in range(n):
            board[j][1] = 1
            if noConflicts(board, j, 1): 
                for k in range(n):
                    board[k][2] = 1
                    if noConflicts(board, k, 2): 
                        for l in range(n):
                            board[l][3] = 1
                            if noConflicts(board, l, 3):
                                print(board)
                            board[l][3] = 0
                    board[k][2] = 0
            board[j][1] = 0
        board[i][0] = 0   
                    

def noConflicts(board, row, col)->bool:
    "We assume the previous queen already there"
    # check the columns
    # we don't need to check the column 
    # because we already did in the main function
    
    # check the rows
    n = len(board)
    r_cnt = 0
    for col_j in range(n):
        if board[row][col_j] == 1:
            r_cnt += 1
    if r_cnt > 1:
        return False
    
    # check diagonal
    # \ direction
    d_cnt = 0
    k = 0
    while row - k >= 0 and col - k >= 0:
        if board[row-k][col-k] == 1:
            d_cnt += 1
        k += 1
    if d_cnt > 1:
        return False
    # / direction
    d_cnt = 0
    k = 0
    while row + k < n and col - k >= 0:
        if board[row+k][col-k] == 1:
            d_cnt += 1
        k += 1
    if d_cnt > 1:
        return False

    return True


board = [
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
        ]

n = len(board)

fourQueens(board, n)
