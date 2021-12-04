def winner(board):
  if(board[0][0]==board[1][1]) and (board[1][1]==board[2][2]) and board[0][0]!=0:
    print(board[0][0],"won")
  elif(board[0][2]==board[1][1]) and (board[1][1]==board[2][0]) and board[2][0]!=0:
    print(board[2][0],"won")
  else:
    for i in range(3):
      if(board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][0]!=0):
        print(board[i][0],"won")
        break
      elif(board[0][i]==board[1][i] and board[1][i]==board[2][i] and board[0][1]!=0):
        print(board[0][i],"won")
        break

board = [[1, 2, 0], [2, 1, 0],[2, 1, 1]]
winner(board)