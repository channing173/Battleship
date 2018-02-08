from Battleship import *

for x in range(5):
  game('p1', x)
  game('p2', x)
  game_over(x)
  turns('p1', x)
  turns('p2', x)
  result(x)
