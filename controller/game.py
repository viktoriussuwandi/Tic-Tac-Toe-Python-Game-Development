from controller.player import Player

class Game :
  def __init__(self) :
    self.game_no    = 0
    self.layout     = []
    self.player = Player(role="X")
    self.comp   = Player()
    self.game_start = True
    self.game_over  = False