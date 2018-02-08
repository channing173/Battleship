from random import randint

boards = {

  'p1': [],
  'p2': []

  }

for x in range(0, 10):
  boards['p1'].append(["0"] * 10)
  boards['p2'].append(["0"] * 10)

def print_board(player):
  for row in boards[player]:
    print " ".join(row)

print "Player One"
print_board('p1')
print ""
print "Player Two"
print_board('p2')

def random_row(player):
  return randint(0, len(boards[player]) - 1)

def random_col(player):
  return randint(0, len(boards[player][0]) - 1)

ships = {

  'p1': [[], []],
  'p2': [[], []]

  }

def make_ships(player):
  for x in range(6):
    r = random_row(player)
    c = random_col(player)
    ships[player][0].append(r)
    ships[player][1].append(c)
    boards[player][r][c]= "-"

make_ships('p1')
make_ships('p2')

sunk = [0, 0]

def game(player, turn):
  if player == 'p1':
    print "Player 1: Turn", turn + 1
  else:
    print "Player 2: Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if guess_row in range(10) and guess_col in range(10) and boards[player][guess_row][guess_col] == "-":
    print "Congratulations! You sank a battleship!\n"
    boards[player][guess_row][guess_col] = "X"
    if player == 'p1':
        sunk[0] = sunk[0] + 1
    else:
        sunk[1] = sunk[1] + 1
  else:
    if guess_row not in range(10) or \
      guess_col not in range(10):
      print "Oops, that's not even in the ocean.\n"
    elif boards[player][guess_row][guess_col] == "X":
      print "You guessed that one already.\n"
    else:
      print "You missed my battleship!\n"
      boards[player][guess_row][guess_col] = "X"
    
def turns(player, turn):
    if turn == 4:
        if player == 'p1':
          print "Player One"
          print_board(player)
          print "Ship locations:"
          for x in range(len(ships[player][0]) - 1):
            print ships[player][0][x], ships[player][1][x]
          print "Ships sunk:", sunk[0], "\n"
        else:
          print "Player Two"
          print_board(player)
          print "Ship locations:"
          for x in range(len(ships[player][0]) - 1):
            print ships[player][0][x], ships[player][1][x]
          print "Ships sunk:", sunk[1], "\n"

def game_over(turn):
    if turn == 4:
        print "Game Over"
        print "----------------------------"

def result(turn):
    if turn == 4:
        if sunk[0] > sunk[1]:
            print "Player One is the winner!"
        elif sunk[1] > sunk[0]:
            print "Player Two is the winner!"
        else:
            print "It's a tie!"


