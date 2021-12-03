def rooks_are_safe(board):
    # Recursion
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                if check_horizontal(board, row, col) or check_vertical(
                        board, col, row):
                    return False

    return True


def check_horizontal(board, row, col):
    "Return True if it encounters other rookie in its horizontal path"
    for i in range(len(board)):
        if i != col and board[row][i] == 1:
            return True


def check_vertical(board, col, row):
    "Return True if it encounters other rookies in its vertical path"
    for i in range(len(board)):
        if board[i][col] == 1 and i != row:
            return True


board = [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
print(rooks_are_safe(board))
