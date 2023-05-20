from controller.player import Player
import math
import os

clear = lambda: os.system('clear')

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

# ----------------------------------------------------------------------------------
# START THE GAME
# ----------------------------------------------------------------------------------
  def start_game(self) :
    # select difficulties & role
    while not self.game_start :
      while self.game_level  == None : self.select_game_level()
      while self.player.role == None : self.select_player_role()
      self.game_start = True

  def select_game_level(self) :
    print('Game level :')
    for i in range(len(self.level_options)) : print(f'{i+1}.{self.level_options[i]}')
    user_input = input('Please select game difficulties : ')
    correct_input = (user_input.isnumeric() and int(user_input) in range(1,4))
    if not correct_input : self.game_level = None; clear()
    else : clear(); self.game_level = int(user_input) - 1

  def select_player_role(self) :
    print('Player Role :')
    for i in range(len(self.role_options)) : print(f'{i+1}.{self.role_options[i]}')
    user_input   = input('Please Player Role (X or O) : ')
    correct_input = (user_input.isnumeric() and int(user_input) in range(1,3))
    if not correct_input : self.player.role = None; clear()
    else :
      clear()
      self.player.role = int(user_input) - 1
      self.comp.role = 1 if self.player.role == 0 else 0

# ----------------------------------------------------------------------------------
# RUNNING THE GAME
# ----------------------------------------------------------------------------------
  def game_loop(self) :
    while not self.game_over :
      clear()
      print(self)
      self.game_over = True
  
  def update_score(self) :
    self.player.score = 0
    self.comp.score   = 0
    
  def update_board(self) :
    rows  = self.get_board()['row']
    cols  = self.get_board()['col']
    board = ''
    for row in range(rows) : 
      board += '\n'
      for col in range(cols) : board += f'    {col}'
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
    