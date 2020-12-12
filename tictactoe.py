"""
Tic Tac Toe Player
"""
"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    
    # loop throught the cells

    # x = 0
    # o = 0

    # for row in board:
    #     for cell in row:
    #         if cell == X:
    #             x += 1
    #         if cell == O:
    #             o += 1
    
    # if x <= o:
    #     return X
    # else:
    #     return O
    empty_board = True
    count_x = 0
    count_o = 0
    f_list = []

    """
    for cell in board:
        empty_board = all(c is None for c in cell)
        print(all(c is None for c in cell))
    """

    # Check every item in board.
    # Flatten list, and put all elements in new list, for later use
    # Check if any of the cells contain X or O. If so, the board is not empty,
    # game has began, so we switch empty_board to False
    for cell in board:
        for i in cell:
            f_list.append(i)
            if i == X or i == O:
                empty_board = False

    # If board is empty, return X as the first player
    # else, figure out who's turn is next, by counting how many X and O's on the game board.
    if empty_board == True:
        return X
    else:
        count_x = f_list.count("X")
        count_o = f_list.count("O")
        if count_x > count_o:
           # print("Computer turn")
            return O
        else:
           # print("Player turn")
            return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    action_set = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                action_set.add((i, j))
    return action_set

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    if action not in actions(board):
        raise ValueError

    new = copy.deepcopy(board)
    new[action[0]][action[1]] = player(new)

    return new


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        elif board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
        elif board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
        elif board[0][2] == board[1][1] == board[2][0]:
            return board[0][2]

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if winner(board) is not None or not actions(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    win = winner(board)

    if win == X:
        return 1
    elif win == None:
        return 0
    else:
        return -1


def get_value(currentPlayer):
    if currentPlayer == X:
        return float("-inf")
    else:
        return float("inf")


def mHelper(board, best):
    """
    Returns the best move value for every
    recursive minimax function.
    Alpha-Beta pruning used from lecture 0...
    """

    if terminal(board):
        return utility(board)
    
    current = player(board)
    value = get_value(current)
    
    for action in actions(board):
        newVal = mHelper(result(board, action), value)

        if current == X:
            if newVal > best:
                return newVal

            value = max(value, newVal)
        
        if current == O:
            if newVal < best:
                return newVal
            
            value = min(value, newVal)
    
    return value






def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    # hard-code the first move
    if board == initial_state():
        return 0, 1
    
    current = player(board)
    value = get_value(current)

    for action in actions(board):
        newVal = mHelper(result(board, action), value)

        if current == X:
            newVal = max(value, newVal)
        if current == O:
            newVal = min(value, newVal)
        
        if newVal != value:
            value = newVal
            best_action = action
    
    return best_action
