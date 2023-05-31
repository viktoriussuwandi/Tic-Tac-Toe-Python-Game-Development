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
     select_cells is not None and len(select_cells) >= self.row and len(select_cells) >= self.col
    ) else []

    if len(cells) < self.row or len(cells) < self.col : return False
    else :
      # Find all combination of cells selected
      cell_pairs     = [ list(a) for a in list( combinations(cells, 3) ) ]

      # Identify if any sum of combination [sum of row, sum of col] is match with any of sum_winner

      find_winner_pair = [
        [a,b,c] for [a,b,c] in cell_pairs if
        [ sum( [a[0],b[0],c[0]] ), sum( [a[1],b[1],c[1]] ) ] in self.sum_winner
      ]

      winner_pair = find_winner_pair[0] if (
        find_winner_pair is not None and 
        len(find_winner_pair) > 0
      ) else []

      if len(winner_pair) > 0:
        # Winner_found is True if :
        # 1. index of all winner_pair cells are even and 
        #    [sum of winner_pair_row, sum of winner_pair_col] in winner_pair is [3,3]] 
        # 2. index of all winner_pair cells are odd and
        #    (cells has identical row or has identical col)

        #a.Check if index of all winner_pair cells are odd or even
        odd_index_selected = [ self.all_cells.index(cell) % 2 == 1 for cell in winner_pair if
                              self.all_cells.index(cell) % 2 == 1 ]
        even_index_selected = [ self.all_cells.index(cell) % 2 == 0 for cell in winner_pair if
                               self.all_cells.index(cell) % 2 == 0 ]
        cells_are_odd  = len(odd_index_selected)  == self.row and len(odd_index_selected)  == self.col
        cells_are_even = len(even_index_selected) == self.row and len(even_index_selected) == self.col

        #b.Check if sum of cells_row, sum of cells_col] in winner_pair is [3,3]
        is_twin = [
          sum( [ cell[0] for cell in winner_pair ] ),
          sum( [ cell[1] for cell in winner_pair ] )
        ] == [3,3]

        #c.Check if (cells has identical row or cells has identical col)

        return f'''
        Winner pair : { winner_pair }
        is Odd      : { cells_are_odd }
        is Even     : { cells_are_even }
        Twin        : { is_twin }
        '''

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
  
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
