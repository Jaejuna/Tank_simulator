def predict(self,board,side):
      model = load_model("chess_model")
      translated = translate_board(board)

      move_matrix = model(translated.reshape(1,8,8,12))[0][0]
      move_matrix = filter_legal_moves(board,move_matrix)
      move= np.unravel_index(np.argmax(move_matrix, axis=None), move_matrix.shape)
      move = chess.Move(move[0],move[1])
      return move,1