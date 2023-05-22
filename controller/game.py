from controller.player import Player
import math

class Game :
  def __init__(self) :
    self.game_no       = 0
    self.layout        = []
    self.game_start    = False
    self.game_over     = False
    self.total_squares = 9
    self.role_options  = ['X', 'O']
    self.level_options = ["Easy", "Medium", "Impossible"]
    self.player = Player()
    self.comp   = Player()
    self.game_level = None
    self.scores     = { "X" : 0, "O" : 0 }

# ----------------------------------------------------------------------------------
# START THE GAME
# ----------------------------------------------------------------------------------
  def start_game(self) :
    check_level_and_role = (
      self.game_level  is not None and 
      self.player.role is not None and 
      self.comp.role   is not None
    )
    self.player.score = 0
    self.comp.score   = 0
    self.game_start = check_level_and_role

  def select_game_level(self, level_selected=None) :
    check_user_input = level_selected is not None and level_selected in self.level_options
    self.game_level  = self.level_options.index(level_selected) if check_user_input else self.game_level
    self.start_game()
    
  def select_player_role(self, role_selected=None) :
    check_user_input  = role_selected is not None and role_selected in self.role_options
    self.player.role  = self.role_options.index(role_selected) if check_user_input else self.player.role
    check_player_is_X = check_user_input and self.player.role == 0
    self.comp.role = None if not check_user_input else 1 if check_player_is_X else 0
    self.start_game()
    
# ----------------------------------------------------------------------------------
# RUNNING THE GAME
# ----------------------------------------------------------------------------------
  def game_loop(self) :
    pass
  
  def update_score(self) :
    self.update_score()
    score_X = self.player.score
    score_O = self.comp.score
    scores = { "X" : score_X, "O" : score_O }
    return scores
    
  def update_board(self) :
    total_squares = self.total_squares
    row = math.sqrt(total_squares)
    col = row
    board = { "row": int(row), "col" : int(col) }
    return board
    
# ----------------------------------------------------------------------------------
# OTHER FUNCTIONS
# ----------------------------------------------------------------------------------  
  def __repr__(self) :
    game_level  = self.level_options[self.game_level]
    player_role = self.role_options[self.player.role]
    comp_role   = self.role_options[self.comp.role]
    return f'''
    Level : {game_level}; (Player : {player_role}; Comp : {comp_role})
    Player cells : {self.player.cells_selected }
    Comp   cells : {self.comp.cells_selected }
    -------------------------------------------
    Board : 
    { self.update_board() }
    '''
    