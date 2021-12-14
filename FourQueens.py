# Check if there is a solution to the problem
# 4 queens optimal

# 1. No queens on the same column
# 2. No queens on the same rows
# 3. No queens on the same diagonal

# board: [-1,-1,-1,-1]
# the result board will look like:
# [1,3,0,2]

# we are going to do this
# column by column


def fourQueens(board, n):
    for i in range(n):
        # print("here")
        board[0] = i
        for j in range(n):
            # print("here")
            board[1] = j
            # 1 is the current column
            # j is the q index
            if noConflicts(board, 1, j): 
                for k in range(n):
                    board[2] = k
                    if noConflicts(board, 2, k): 
                        for l in range(n):
                            board[3] = l
                            if noConflicts(board, 3, l):
                                print(board)
                            board[3] = -1
                    board[2] = -1
            board[1] = -1
        board[0] = -1
                    

def noConflicts(board, current, q_idx)->bool:
    """
    We assume the previous queen already there
    board: [-1,-1,-1,-1]
    q_idx: row index
    current: column index
    """
    # check the columns
    # we don't need to check the column 
    # because we already did in the main function
    
    # check the rows
    # [4,1,4,-1] : return False
    # there is at least 1 duplicate value not -1 (4)
    for i in range(current):
        if board[i] == q_idx:
            return False
    
    # check diagonal
    # both \ and / direction
    # \ direction
    # board = [-1,-1,1,2]
    # abs(1-2) - (2-3) == 0: return False
    # board = [-1,0,-1,2]
    # abs(0-2) == (3-1): return False
    # aka diff of q_idx == diff of current 
    # hold true for / direction
    # board = [3,2,0,0]
    # abs(3-2) == (1-0)
    for i in range(current):
        if abs(board[i] - board[current]) == current - i:
            return False
    return True


board = [0,0,0,0]
n = len(board)

fourQueens(board, n)
