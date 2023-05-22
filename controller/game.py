from controller.player import Player
import math

class Game :
  def __init__(self) :
    self.game_no       = 0
    self.game_start    = False
    self.game_over     = True
    self.total_squares = 9
    
    self.role_options  = ['X', 'O']
    self.level_options = ["Easy", "Medium", "Impossible"]
    
    self.player        = Player()
    self.comp          = Player()
    
    self.game_level    = None
    self.scores        = { "X" : 0, "O" : 0 }
    self.turn          = None
    self.board         = {}

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
  
  def update_score(self) :
    score_X = self.player.score
    score_O = self.comp.score
    game_scores = { "X" : score_X, "O" : score_O }
    self.scores = game_scores
    
  def update_board(self) :
    total_squares = self.total_squares
    row = math.sqrt(total_squares)
    col = row
    game_board = { "row": int(row), "col" : int(col) }
    self.board = game_board
    
  def update_turn(self) :
    if self.game_start == False : self.turn = None
    else :
      player_cells = len(self.player.cells_selected)
      comp_cells   = len(self.comp.cells_selected)
      is_player_turn  = self.player.role == 0 or player_cells < comp_cells
      role_turn    = 0 if is_player_turn else self.comp.role
      self.turn = self.role_options[role_turn]
    
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
    