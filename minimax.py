from checks import who_wins

def maximum(board):
    max_score = -2


    result = who_wins(board)

    if result == 'X':
        return (-1, 0, 0)
    elif result == 'O':
        return (1, 0, 0)
    elif result == '.':
        return (0, 0, 0)

    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == '.':
                board[i][j] = 'O'
                (m, min_i, min_j) = minimum(board)

                if m > max_score:
                    max_score = m
                    row = i
                    column = j

                board[i][j] = '.'
    return (max_score, row, column)

def minimum(board):
    min_score = 2


    result = who_wins(board)

    if result == 'X':
        return (-1, 0, 0)
    elif result == 'O':
        return (1, 0, 0)
    elif result == '.':
        return (0, 0, 0)

    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == '.':
                board[i][j] = 'X'
                (m, max_i, max_j) = maximum(board)
                if m < min_score:
                    min_score = m
                    row = i
                    column = j
                board[i][j] = '.'

    return (min_score, row, column)