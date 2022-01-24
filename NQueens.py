def nQueens(size):
    board = [-1] * size
    if rQueens(board, 0, size):
        print(board)
    else:
        print("No possible solution")

def noConflicts(board, current):
    for i in range(current):
        # check rows
        if board[i] == board[current]:
            return False
        # check diagonal
        if current - i == abs(board[current] - board[i]):
            return False    
    return True


def rQueens(board, current, size):
    if current == size: # put down all 7 queens and no noConflicts
        return True
    else:
        # backtrack Recursion
        for i in range(size):
            board[current] = i
            if noConflicts(board, current):
                done = rQueens(board, current + 1, size)
                if done: 
                    return True
        return False

nQueens(4)
