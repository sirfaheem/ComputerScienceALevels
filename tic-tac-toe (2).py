board = [[" " for i in range(3)] for j in range(3)]

def draw_board():
  print("  0 1 2")
  for i in range(3):
    print(f"{i} {board[i][0]}|{board[i][1]}|{board[i][2]}")
    if i != 2:
      print("  -----")

def get_move(player):
  while True:
    try:
      x = int(input(f"{player}, enter the row for your move: "))
      y = int(input(f"{player}, enter the column for your move: "))
      if x in range(3) and y in range(3) and board[x][y] == " ":
        board[x][y] = player
        break
      else:
        print("Invalid move, try again.")
    except ValueError:
      print("Invalid input, try again.")

def check_winner():
  # check rows
  for row in board:
    if row[0] != " " and row[0] == row[1] == row[2]:
      return row[0]

  # check columns
  for col in range(3):
    if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
      return board[0][col]

  # check diagonals
  if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
    return board[0][0]
  if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
    return board[0][2]

  return " "

def tic_tac_toe():
  draw_board()
  num_moves = 0
  while True:
    get_move("X")
    draw_board()
    winner = check_winner()
    if winner != " ":
      print(f"{winner} wins!")
      break
    num_moves += 1
    if num_moves == 9:
      print("It's a draw!")
      break
    get_move("O")
    draw_board()
    winner = check_winner()
    if winner != " ":
      print(f"{winner} wins!")
      break
    num_moves += 1
    if num_moves == 9:
      print("It's a draw!")
      break

tic_tac_toe()
