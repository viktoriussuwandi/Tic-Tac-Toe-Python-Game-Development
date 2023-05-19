from controller.player import Player
from controller.game   import Game

game   = Game()
player = Player(role="human")
comp   = Player()

def game_test() :
  print(player.mark)
  print(comp.mark)

game_test()