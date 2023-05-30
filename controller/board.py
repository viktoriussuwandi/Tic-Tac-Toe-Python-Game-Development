import math
from itertools import combinations

class Board:

  def __init__(self, total_cells=None):
    self.total_square = total_cells if total_cells is not None else None
    self.row = None
    self.col = None
    self.all_cells  = []
    self.open_cells = []
    self.sum_winner = [ [3,0], [0,3], [3,3], [3,6], [6,3] ] #Winner combination of [ sum(row), sum(col) ]
    self.board_dimmension = {}
    self.create_board()
    self.cell_owners = [None for i in self.all_cells]
    self.print_out = ''

  def check_if_win(self, select_cells = None) :
    cells = select_cells if (
     select_cells is not None and 
     len(select_cells) >= self.row and 
     len(select_cells) >= self.col
    ) else []
    if len(cells) == 0 : return None
    else :
      # Find cell_pairs of cells selected, and sum that pairs
      cell_pairs     = [ list(a) for a in list( combinations(cells, 3) ) ]
      cell_sum_pairs = [ [ sum([a[0],b[0],c[0]]), sum( [a[1],b[1],c[1]]) ] for [a,b,c] in cell_pairs ]

      
      # Identify if cell_sum_pairs is in the list of sum_winner
      winner_pair = []
      for [a,b,c] in cell_pairs :
        winner_pair = [a,b,c] if [ 
          sum([a[0],b[0],c[0]]), sum( [a[1],b[1],c[1]]) 
        ] in self.sum_winner else winner_pair
        
      return f'\n{ winner_pair }'

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
  
  def create_board(self):
    if self.total_square is not None:
      self.row = int(math.sqrt(self.total_square))
      self.col = self.row
      self.all_cells = [
        [row, col] for row in range(self.row) for col in range(self.col)
      ]
      self.board_dimmension = {"row": self.row, "col": self.col}

  def update_board(
    self,
    player_role  = None,
    comp_role    = None,
    player_cells = None,
    comp_cells   = None,
    is_player_selecting = False,
    is_comp_selecting   = False
  ):
    all_cells = self.all_cells
    
    # Update open cells
    selected_cells  = player_cells + comp_cells
    list_open_cells = [ cell for cell in all_cells if cell not in selected_cells]
    self.open_cells = all_cells if len(selected_cells) == 0 else list_open_cells 
    
    # Checking cell's owner
    for i in range(len(all_cells)):
      # Check if cell own by player
      if is_player_selecting:
        for j in range(len(player_cells)):
          player_own = self.cell_owners[i] is None and all_cells[i] == player_cells[j]
          self.cell_owners[i] = player_role if player_own else self.cell_owners[i]

      # Check if cell own by Comp
      if is_comp_selecting:
        for j in range(len(comp_cells)):
          comp_own = self.cell_owners[i] is None and all_cells[i] == comp_cells[j]
          self.cell_owners[i] = comp_role if comp_own else self.cell_owners[i]
    
    # Update attribute to print out board it-self
    self.print_out = ''
    for co in range(len(self.cell_owners)):
      first_col = co % self.row == 0
      if co == 0: self.print_out += f'     {str(self.cell_owners[co])}'
      elif first_col: self.print_out += f'\n     {str(self.cell_owners[co])}'
      else: self.print_out += f' {str(self.cell_owners[co])}'

  def __repr__(self):
    return self.print_out

# ----------------------------------------------------------------------------------
    # winner_sum_required = [ [3,0], [0,3], [3,3], [3,6], [6,3] ]
    
    # Check if the winner is player
    # is_player_win     = False
    # player_cells      = self.player.cells_selected
    # player_cell_pairs = []; player_pair_sum   = []

    # if self.winner_found == False and len(player_cells) >= 3 :
    #   player_cell_pairs = list( combinations(player_cells, 3) )
    #   player_pair_sum = [
    #     [ sum(list((a[0], b[0], c[0]))), sum(list((a[1], b[1], c[1]))) ] for (a,b,c) in player_cell_pairs 
    #   ]
    #   arr_player_pair_sum = [ i for i in winner_sum_required if i in player_pair_sum ]
    #   check_player_pair_sum = len(arr_player_pair_sum) > 0

# ----------------------------------------------------------------------------------
      
      # find the pair cells
      # check of all cells has identic row or cols
      
      # check_player_identic_rowCol = [
      #   ( (a[0] == b[0] == c[0]) or (a[1] == b[1] == c[1]) ) for (a,b,c) in player_cell_pairs
      # ] if arr_player_pair_sum == [3,3] else True

      # ----------------------------------------------------------------------------------
      # is_player_win = check_player_pair_sum and check_player_identic_rowCol
      # if is_player_win == True :
      #   self.winner_found = is_player_win
      #   self.game_over    = True
      #   self.game_start   = False
      #   self.winner       = {'Role' : 'Player', 'Mark' : self.game_roles['Player']}
