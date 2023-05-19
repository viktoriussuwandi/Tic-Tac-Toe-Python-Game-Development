from controller.player import Player
import math

class Game :
  def __init__(self) :
    self.game_no    = 0
    self.layout     = []
    self.player     = Player(role="X")
    self.comp       = Player()
    self.game_start = True
    self.game_over  = False
    self.total_squares = 9
    self.difficult_options = ["Easy", "Medium", "Impossible"]

  def get_board(self) :
    total_squares = self.total_squares
    row = math.sqrt(total_squares)
    col = row
    board = { "row": int(row), "col" : int(col) }
    return board

  def get_score(self) :
    self.update_score()
    score_X = self.player.score
    score_O = self.comp.score
    scores ={ "X" : score_X, "O" : score_O }
    return scores
  
  def update_score(self) :
    self.player.score = 0
    self.comp.score   = 0