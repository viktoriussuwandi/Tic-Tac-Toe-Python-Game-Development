from controller.player import Player
from controller.board import Board
import random

import os
clear_screen = lambda: os.system('clear')

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
    
    self.comp_autoCell  = {'cell': [], 'index': None}

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
    self.board_open_cells = 0

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

    self.comp_autoCell  = {'cell': [], 'index': None}

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
    self.board_open_cells = 0
    self.game_update_attr()
    
# ----------------------------------------------------------------------------------
# START THE GAME
# ----------------------------------------------------------------------------------

  def game_loop(self) :
    self.update_score()
    self.update_turn()
    self.update_board()
    print(self)

  def game_update_attr(self):
    is_in_game = self.game_start == True and self.game_over == False
    if not is_in_game : self.start_game()

    #Trigger to run function for comp auto cell selected
    if ( self.winner_found == False and self.turn == self.comp.role and 
         self.turn_name == 'Comp' ) : self.cell_choose_by_comp()
           
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
    if   self.turn_name == 'Player': 
      self.player.cells_selected.append([row, col])
      self.update_winner(self.player.cells_selected)
    elif self.turn_name == 'Comp'  : 
      self.comp.cells_selected.append([row, col])
      self.update_winner(self.comp.cells_selected)
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
        player_role         = player_role_select, 
        comp_role           = comp_role_select,
        player_cells        = player_cells_select,
        comp_cells          = comp_cells_select,
        is_player_selecting = is_player_select,
        is_comp_selecting   = is_comp_select
      )
      
      #Update board open cells attribute
      self.board_open_cells = len(self.board.open_cells)      

  def update_winner(self, cells = None):
    cells_check = cells if (
      cells is not None and 
      len(cells) >= self.board.row and 
      len(cells) >= self.board.col
    ) else []
    
    if self.winner_found == False and len(cells_check) >= 3 :
      # clear_screen()
      is_winner_found = self.board.identify_cells(cells_check)
      if is_winner_found == True :
        self.winner_found   = is_winner_found
        self.winner['Role'] = self.turn_name
        self.winner['Mark'] = self.turn_mark

# ----------------------------------------------------------------------------------
# OTHER FUNCTIONS
# ----------------------------------------------------------------------------------

  def cell_choose_by_comp(self):
    cell_choosen = []
    cell_index   = None
    open_cells = self.board.open_cells
    if len(open_cells) == 1 : 
      cell_choosen = self.board.open_cells[0]
    else : cell_choosen = random.choice(open_cells)
      
    cell_index = self.board.all_cells.index(cell_choosen)
    self.comp_autoCell["cell"]  = cell_choosen
    self.comp_autoCell["index"] = cell_index

  def __repr__(self):
    print_board = self.board.print_out
    open_cells  = self.board.open_cells
    
    #-------------------------------------------------------------------
    #-------------------------------------------------------------------
    found_winner = f'''
    -----------------CONGRATULATIONS !!--------
     Winner       : {self.winner['Mark']} ( {self.winner['Role']} )
    -------------------------------------------
     Level        : {self.game_level_txt}
    ===========================================
     Board :\n{print_board}'''
    
    #-------------------------------------------------------------------
    #-------------------------------------------------------------------
    not_found_winner = f'''
    -----------------TIC TAC TOE GAME----------
     Current Turn : {self.turn_mark} - {self.turn_name}
     Board :\n{print_board}
    ===========================================
     Winner       : {self.winner}
     Open cells   : 
     {open_cells}
    ------------------------------------------- 
     Level        : {self.game_level_txt}; 
     Roles        : {self.game_roles}
     Player cells : {self.player.cells_selected }
     Comp   cells : {self.comp.cells_selected }
    -------------------------------------------'''

    
    #-------------------------------------------------------------------
    #-------------------------------------------------------------------
    clear_screen()
    return found_winner if self.winner_found == True else not_found_winner