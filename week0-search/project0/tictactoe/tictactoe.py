"""
Tic Tac Toe Player
"""

import math
from typing import List, Set

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
    number_of_X = 0
    number_of_O = 0
    for row in board:
        for col in row:
            if col == X:
                number_of_X += 1
            elif col == O:
                number_of_O += 1
            else:
                pass

    if number_of_X == number_of_O:
        return X
    else:
        return O
            


def actions(board: List[List[str | None]]) -> Set[tuple[int, int]]:
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for row_index, row in enumerate(board):
        for col_index, col in enumerate(row):
            if col == EMPTY:
                possible_actions.add((row_index, col_index))

    return possible_actions
    


def result(board: List[List[str | None]], action: tuple[int, int]):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    turn = player(board)
    row = action.index(0)
    column = action.index(1)

    if row > 2 or column > 2 or board[row][column] != EMPTY:
        raise Exception("Invalid move")
    
    board[row][column] = turn
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    # If a row is filled by X or O
    for row in board:
        for col in row:
            ...

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
