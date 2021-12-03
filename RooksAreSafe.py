from collections import Counter


def rooks_are_safe(board):
    # O(n^2)
    # checking the rows
    for row in range(len(board)):
        cnt = Counter(board[row])
        if cnt[1] > 1: return False
    
    col_dict = dict()
    # {0:0, 1: 1, 2:1, 3: 1}
    # Check the columns
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                col_dict[col] = col_dict.get(col, 0) + 1
                if col_dict[col] > 1: return False
    return True
