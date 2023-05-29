from controller.player import Player
from controller.board import Board
from itertools import combinations

import os
clear_screen = lambda: os.system('clear')

import random

class Game:

  def __init__(self): 
    self.game_no    = 0
    self.game_start = False
    self.game_over  = True

    self.role_options  = ['X', 'O']
    self.game_roles    = {'Player' : '', 'Comp' : ''}
    self.level_options = ["Easy", "Medium", "Impossible"]

    self.player = Player()
    self.comp   = Player()
    self.board  = Board(9)

    self.game_level     = None
    self.game_level_txt = ''
    self.scores         = {"X": 0, "O": 0}
    
    self.winner       = {'Role' : '', 'Mark' : ''}
    self.winner_found = False
    
    self.turn      = None
    self.turn_name = None  #Game role : Player or comp
    self.turn_mark = None  #Game mark : X or O

    self.board_printed    = ''
    self.board_dimmension = {}

  def refresh_attr(self) :
    self.game_no    = 0
    self.game_start = False
    self.game_over  = True

    self.role_options  = ['X', 'O']
    self.game_roles    = {'Player' : '', 'Comp' : ''}
    self.level_options = ["Easy", "Medium", "Impossible"]

    self.player = Player()
    self.comp   = Player()
    self.board  = Board(9)

    self.game_level     = None
    self.game_level_txt = ''
    self.scores         = {"X": 0, "O": 0}
    
    self.winner       = {'Role' : '', 'Mark' : ''}
    self.winner_found = False
    
    self.turn      = None
    self.turn_name = None  #Game role : Player or comp
    self.turn_mark = None  #Game mark : X or O

    self.board_printed    = ''
    self.board_dimmension = {}
# ----------------------------------------------------------------------------------
# START THE GAME
# ----------------------------------------------------------------------------------

  def game_loop(self) :
    self.update_score()
    self.update_winner()
    self.update_turn()
    self.update_board()

    print(self)
    
  def game_update_attr(self):
    is_in_game = self.game_start == True and self.game_over == False
    if not is_in_game : self.start_game()
    elif (is_in_game and self.winner_found == True) : self.refresh_attr();
    self.game_loop()
    
  def start_game(self):
    check_level_and_role = (
      self.game_level  is not None and 
      self.player.role is not None and 
      self.comp.role   is not None
    )
    self.game_start = check_level_and_role
    self.game_over  = not check_level_and_role

# ----------------------------------------------------------------------------------
# USER INTERACTIONS
# ----------------------------------------------------------------------------------

  def select_game_level(self, level_selected = None):
    check_user_input = level_selected is not None and level_selected in self.level_options
    self.game_level = self.level_options.index(
      level_selected) if check_user_input else self.game_level
    self.game_level_txt = level_selected
    self.game_update_attr()

  def select_player_role(self, role_selected = None):
    check_user_input = role_selected is not None and role_selected in self.role_options
    self.player.role = self.role_options.index(
      role_selected) if check_user_input else self.player.role
    check_player_is_X = check_user_input and self.player.role == 0
    self.comp.role = None if not check_user_input else 1 if check_player_is_X else 0
    self.game_roles['Player'] = self.role_options[ int(self.player.role) ]
    self.game_roles['Comp']   = self.role_options[ int(self.comp.role) ]
    self.game_update_attr()

  def select_cells(self, row = None, col = None):
    if   self.turn_name == 'Player': self.player.cells_selected.append([row, col])
    elif self.turn_name == 'Comp'  : self.comp.cells_selected.append([row, col])
    self.game_update_attr()

# ----------------------------------------------------------------------------------
# UPDATE GAME ATTRIBUTE
# ----------------------------------------------------------------------------------

  def update_turn(self):
    if self.game_start == False and self.game_over == True : self.turn = None
    else :
      player_cells   = len(self.player.cells_selected)
      comp_cells     = len(self.comp.cells_selected)
      is_player_turn = player_cells < comp_cells or ( self.player.role == 0 and player_cells == comp_cells )
 
      self.turn      = self.player.role if is_player_turn else self.comp.role
      self.turn_name = 'Player' if is_player_turn else 'Comp'
      self.turn_mark = self.role_options[self.turn]

  def update_score(self):
    score_X     = self.player.score
    score_O     = self.comp.score
    game_scores = {"X": score_X, "O": score_O}
    self.scores = game_scores

  def update_board(self):
    is_in_game = self.game_start == True and self.game_over == False
    if is_in_game == False : self.board_dimmension = self.board.board_dimmension
    else :
      player_role_select = None if self.player.role is None else self.role_options[ int(self.player.role) ]
      comp_role_select   = None if self.comp.role   is None else self.role_options[ int(self.comp.role) ]
  
      is_player_select = len(self.player.cells_selected) > 0
      is_comp_select   = len(self.comp.cells_selected)   > 0
      
      player_cells_select = self.player.cells_selected
      comp_cells_select   = self.comp.cells_selected
    
      self.board.update_board(
        player_role  = player_role_select, 
        comp_role    = comp_role_select,
        
        player_cells = player_cells_select,
        comp_cells   = comp_cells_select,
        
        is_player_selecting = is_player_select,
        is_comp_selecting   = is_comp_select
    )
      # self.game_update_attr()
      
    #--------------------------------------------------------------------------------------------------
    # CHEKING
    #--------------------------------------------------------------------------------------------------
    # test = f'''
    # Winner       : {self.winner}
    # Open cells   : {self.board.open_cells}
    # Player cells : {self.player.cells_selected }
    # Comp   cells : {self.comp.cells_selected }
    # '''  
    # clear_screen()
    # print(test)
    #--------------------------------------------------------------------------------------------------
  
  def update_winner(self):
    winner_sum_required = [ [3,0], [0,3], [3,3], [3,6], [6,3] ]
    
    # Check if the winner is player
    is_player_win     = False
    player_cells      = self.player.cells_selected
    player_cell_pairs = []; player_pair_sum   = []

    if self.winner_found == False and len(player_cells) >= 3 :
      player_cell_pairs = list( combinations(player_cells, 3) )
      player_pair_sum = [
        [ sum(list((a[0], b[0], c[0]))), sum(list((a[1], b[1], c[1]))) ] for (a,b,c) in player_cell_pairs 
      ]
      arr_player_pair_sum = [ i for i in winner_sum_required if i in player_pair_sum ]
      check_player_pair_sum = len(arr_player_pair_sum) > 0
      # ----------------------------------------------------------------------------------
      
      # find the pair cells
      # check of all cells has identic row or cols
      
      check_player_identic_rowCol = [
        ( (a[0] == b[0] == c[0]) or (a[1] == b[1] == c[1]) ) for (a,b,c) in player_cell_pairs
      ] if arr_player_pair_sum == [3,3] else True
      # ----------------------------------------------------------------------------------
      is_player_win = check_player_pair_sum and check_player_identic_rowCol
      if is_player_win == True :
        self.winner_found = is_player_win
        self.game_over    = True
        self.game_start   = False
        self.winner       = {'Role' : 'Player', 'Mark' : self.game_roles['Player']}
    
    # Check if the winner is comp
    is_comp_win     = False
    comp_cells      = self.comp.cells_selected
    comp_cell_pairs = []; comp_pair_sum   = []

    if self.winner_found == False and len(comp_cells) >= 3 :
      comp_cell_pairs = list( combinations(comp_cells, 3) )
      comp_pair_sum = [
        [ sum(list((a[0], b[0], c[0]))), sum(list((a[1], b[1], c[1]))) ] for (a,b,c) in comp_cell_pairs 
      ]
      arr_comp_pair_sum = [ i for i in winner_sum_required if i in comp_pair_sum ]
      check_comp_pair_sum = len(arr_comp_pair_sum) > 0
      # ----------------------------------------------------------------------------------
      check_comp_identic_rowCol = True
      # ----------------------------------------------------------------------------------
      is_comp_win = check_comp_pair_sum and check_comp_identic_rowCol
      if is_comp_win == True :
        self.winner_found = is_comp_win
        self.game_over    = True
        self.game_start   = False
        self.winner       = {'Role' : 'Comp', 'Mark' : self.game_roles['Comp']}

# ----------------------------------------------------------------------------------
# OTHER FUNCTIONS
# ----------------------------------------------------------------------------------

  def cell_choose_by_comp(self): return random.choice(self.board.open_cells)

  def __repr__(self):
    print_board     = self.board.print_out
    found_winner = f'''
    -----------------CONGRATULATIONS !!--------
     Winner       : {self.winner}
    ------------------------------------------- 
     Level        : {self.game_level_txt}; {self.game_roles})
    -------------------------------------------
    ===========================================
     Board :\n{print_board}'''
    
    not_found_winner = f'''
    -----------------TIC TAC TOE GAME----------
     Winner       : {self.winner}
     Open cells   : 
     {self.board.open_cells}
    ------------------------------------------- 
     Level        : {self.game_level_txt}; {self.game_roles})
    (Game start   : {self.game_start}) ; (Game over : {self.game_over})
     Player cells : {self.player.cells_selected }
     Comp   cells : {self.comp.cells_selected }
    -------------------------------------------
     Current Turn : {self.turn_mark} - {self.turn_name}
    ===========================================
     Board :\n{print_board}'''
    
    clear_screen()
    # return found_winner if self.winner_found == True else not_found_winner
    return not_found_winner