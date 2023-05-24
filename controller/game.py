from controller.player import Player
from controller.board  import Board

class Game :
  def __init__(self) :
    self.game_no       = 0
    self.game_start    = False
    self.game_over     = True

    self.role_options  = ['X', 'O']
    self.level_options = ["Easy", "Medium", "Impossible"]
    
    self.player        = Player()
    self.comp          = Player()
    self.board         = Board(9)
    
    self.game_level    = None
    self.scores        = { "X" : 0, "O" : 0 }
    self.turn          = None
    self.turn_name     = None #Game role : Player or comp
    self.turn_mark     = None #Game mark : X or O

    self.board_printed = ''
    self.board_current = {}
    

# ----------------------------------------------------------------------------------
# START THE GAME
# ----------------------------------------------------------------------------------
  def game_update_attr(self) :
    if self.game_start == False and self.game_over == True : self.start_game()
    self.update_turn()
    self.update_score()
    self.update_board()
    if self.game_start == True and self.game_over == False : 
      self.print_board()
      print(self)
      
  def start_game(self) :
    check_level_and_role = (
      self.game_level  is not None and 
      self.player.role is not None and 
      self.comp.role   is not None
    )
    self.player.score = 0
    self.comp.score   = 0
    self.game_start = check_level_and_role
    self.game_over  = not check_level_and_role

# ----------------------------------------------------------------------------------
# USER INTERACTIONS
# ----------------------------------------------------------------------------------
  def select_game_level(self, level_selected=None) :
    check_user_input = level_selected is not None and level_selected in self.level_options
    self.game_level  = self.level_options.index(level_selected) if check_user_input else self.game_level
    self.game_update_attr()
    
  def select_player_role(self, role_selected=None) :
    check_user_input  = role_selected is not None and role_selected in self.role_options
    self.player.role  = self.role_options.index(role_selected) if check_user_input else self.player.role
    check_player_is_X = check_user_input and self.player.role == 0
    self.comp.role = None if not check_user_input else 1 if check_player_is_X else 0
    self.game_update_attr()

  def select_cells(self, row = None, col = None) :
    if   self.turn_name == 'Player' : self.player.cells_selected.append([row,col])
    elif self.turn_name == 'Comp'   : self.comp.cells_selected.append([row,col])
    self.game_update_attr()
    
# ----------------------------------------------------------------------------------
# UPDATE GAME ATTRIBUTE
# ----------------------------------------------------------------------------------

  def update_score(self) :
    score_X = self.player.score
    score_O = self.comp.score
    game_scores = { "X" : score_X, "O" : score_O }
    self.scores = game_scores

  def update_turn(self) :
    if self.game_start == False and self.game_over == True :
      self.turn = None
    else :
      player_cells   = len(self.player.cells_selected)
      comp_cells     = len(self.comp.cells_selected)
      is_player_turn = player_cells < comp_cells or (self.player.role == 0 and player_cells == comp_cells)
      self.turn      = self.player.role if is_player_turn else self.comp.role
      self.turn_name = 'Player' if is_player_turn else 'Comp'
      self.turn_mark = self.role_options[self.turn]
   
  def update_board(self) :
    if   self.game_start == False and self.game_over == True  : self.board_current = self.board.starting_board 
    elif self.game_start == True  and self.game_over == False : self.board_current = self.board.update_board()

# ----------------------------------------------------------------------------------
# OTHER FUNCTIONS
# ----------------------------------------------------------------------------------

  def print_board(self) :
    self.board_printed = ''
    if self.board_current == {} :
      self.board_printed += 'no board printed'
    else :
      player_role = None if self.player.role is None else self.role_options[ int(self.player.role) ]
      comp_role   = None if self.comp.role   is None else self.role_options[ int(self.comp.role) ]
      
      # check if cell is own by player or comp
      all_cells    = self.board.all_cells
      cell_owners  = [ None for i in all_cells ]
      player_cells = self.player.cells_selected
      comp_cells   = self.comp.cells_selected
      
      # check if player or comp already select one cell (at least)
      is_player_selecting = len(self.player.cells_selected) > 0
      if is_player_selecting :
        for i in range(len(player_cells)) :
          for j in range(len(all_cells)) :
            check_last_owner = all_cells[j] == None and player_cells[i] == all_cells[j]
            cell_owners[j]   = player_role if check_last_owner else None
          
      is_comp_selecting = len(self.comp.cells_selected) > 0
      if is_comp_selecting :
        for i in range(len(comp_cells)) :
          for j in range(len(all_cells)) :
            check_last_owner = all_cells[j] == None and comp_cells[i] == all_cells[j]
            cell_owners[j] = comp_role if check_last_owner else None
      
      self.board_printed +=f'''
     cell_owners  : {cell_owners}
     '''
    
  def __repr__(self) :
    game_level  = None if self.game_level  is None else self.level_options[ int(self.game_level) ]
    player_role = None if self.player.role is None else self.role_options[ int(self.player.role) ]
    comp_role   = None if self.comp.role   is None else self.role_options[ int(self.comp.role) ]
    return f'''
    -----------------TIC TAC TOE GAME----------
     Level        : {game_level}; (Player : {player_role} ; Comp : {comp_role})
    (Game start   : {self.game_start}) ; (Game over : {self.game_over})
     Player cells : {self.player.cells_selected }
     Comp   cells : {self.comp.cells_selected }
    -------------------------------------------
     Current Turn : {self.turn_mark} - {self.turn_name}
    ===========================================
     Board : 
     { self.board_printed }
    '''