import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow
from hybrid_algo import *
from IPython.display import display, HTML, clear_output
from time import sleep

board = chess.Board()
sides = ['White','Black']
engine = ChessEngine(algorithms = [MinMaxTree,NeuralNetwork])

def display_board(board, use_svg):
    if use_svg:
        return board._repr_svg_()
    else:
        return "<pre>" + str(board) + "</pre>"
    
moves = []
pgn = ''
counter = 1
for i in range(100):
    if i % 2 == 0:
        pgn += str(counter)+ '.'
        counter += 1
        
    side = sides[i%2]
    move = engine.generate_move(board,side)
    string = str(board.san(move))+' '
    pgn+=string
    
    board.push(move)
    html = display_board(board, True)
    display(HTML(html))
    sleep(1)
    
    if board.is_game_over():
        break