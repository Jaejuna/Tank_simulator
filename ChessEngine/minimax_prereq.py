import chess
from board_conversion import *

def material_counter(board):
    material = np.array([0,0])
    translated_board = board_matrix(board)
    for piece in translated_board:
        material += value_dict[piece]
    return material

def pos_cont(board):
    boards = []
    legal_moves = list(board.legal_moves)
    for move in legal_moves:
        copy_board = board.copy()
        copy_board.push(move)
        boards.append(copy_board)
    return boards,legal_moves