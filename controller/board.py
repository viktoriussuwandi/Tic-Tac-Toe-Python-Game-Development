import math
from itertools import combinations

class Board:

  def __init__(self, total_cells=None):
    self.total_square = total_cells if total_cells is not None else None
    self.row = None
    self.col = None
    self.all_cells  = []
    self.open_cells = []

    #Winner combination of [ sum(row), sum(col) ]
    self.sum_winner = [ 
      [3,0], [0,3], [3,3], [3,6], [6,3] 
    ] 
    
    self.board_dimmension = {"row": 0, "col": 0}
    self.create_board()
    self.cell_owners = [None for i in self.all_cells]
    self.print_out = ''

#----------------------------------------------------------------------------------------------------
# CREATE AND UPDATE BOARD
#----------------------------------------------------------------------------------------------------

  def update_printOut(self):
    self.print_out = 'Working on printout\n'
    self.print_out = '---------------------'
    start_space = ('').join([' ' for i in range(5)])
    output = ''
    for i in range(self.row) :
      row = []
      for j in range(self.col) :
        idx  = (self.row*i) + j
        char = str(self.cell_owners[idx])
        row.apend(char)
      
    
    # self.print_out = ''
    # idx  = 0
    # char_space = ' '
    # long_space = ('').join([' ' for i in range(5)])
    # for i in range(self.row) :
    #   for j in range(self.col) :
    #     idx  = (self.row*i) + j
    #     char = str(self.cell_owners[idx])
    #     self.print_out += f'{long_space}{char}{char_space}'
    #   self.print_out +='\n'

  def create_board(self):
    if self.total_square is not None:
      self.row = int(math.sqrt(self.total_square))
      self.col = self.row
      self.all_cells = [
        [row, col] for row in range(self.row) for col in range(self.col)
      ]
      self.board_dimmension["row"] = self.row
      self.board_dimmension["col"] = self.col

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
      self.update_printOut()

#----------------------------------------------------------------------------------------------------
# WINNER CHECKING
#----------------------------------------------------------------------------------------------------
  def identify_cells(self, select_cells = None) :
    cells = select_cells if (
     select_cells is not None and len(select_cells) >= self.row and len(select_cells) >= self.col
    ) else []

    if len(cells) < self.row or len(cells) < self.col : return False
    else :
      # Find all combination of cells selected
      cell_pairs = [ list(a) for a in list( combinations(cells, 3) ) ]

      # Identify if any sum of combination [sum of row, sum of col] is match with any of sum_winner
      find_winner_pair = [
        [a,b,c] for [a,b,c] in cell_pairs if
        [ sum( [a[0],b[0],c[0]] ), sum( [a[1],b[1],c[1]] ) ] in self.sum_winner
      ]

      winner_pair = find_winner_pair[0] if (
        find_winner_pair is not None and len(find_winner_pair) > 0
      ) else []

      if len(winner_pair) > 0:
        #a.Check if index of all winner_pair cells are odd or even
        odd_index_winner_cell = [
          self.all_cells.index(cell) % 2 == 1 for cell in winner_pair if self.all_cells.index(cell) % 2 == 1 ]
        even_index_winner_cell = [
          self.all_cells.index(cell) % 2 == 0 for cell in winner_pair if self.all_cells.index(cell) % 2 == 0 ]
        are_cells_odd  = ( len(odd_index_winner_cell)  == self.row and len(odd_index_winner_cell) )  == self.col
        are_cells_even = ( len(even_index_winner_cell) == self.row and len(even_index_winner_cell) ) == self.col

        #b.Check if sum of cells_row, sum of cells_col] in winner_pair is [3,3]
        is_twin = [
          sum( [ cell[0] for cell in winner_pair ] ),
          sum( [ cell[1] for cell in winner_pair ] )
        ] == [3,3]

        #c.Check if (cells has identical row or cells has identical col)
        row_winner_cells = [ cell[0] for cell in winner_pair ]
        col_winner_cells = [ cell[1] for cell in winner_pair ]
        is_horizontal_align = len([ c for c in row_winner_cells[1:] if c == row_winner_cells[0] ]) > 0
        is_vertical_align   = len([ c for c in col_winner_cells[1:] if c == col_winner_cells[0] ]) > 0
        
        return self.winner_checking(
          identify_odd  = are_cells_odd, 
          identify_even = are_cells_even, 
          identify_twin = is_twin, 
          identify_horizontal = is_horizontal_align, 
          identify_vertical = is_vertical_align
        )

  def winner_checking( self, identify_odd, identify_even, identify_twin, 
                       identify_horizontal, identify_vertical ):
    # Winner_found is True if :
    # 1. win Diagonally : 
    #    index of all winner_pair cells are even and
    #    has twin conbination of [sum of winner_pair_row, sum of winner_pair_col] in winner_pair, 
    #    example : [3,3]
    win_diagonally = ( identify_odd == False and identify_even == True and 
                       identify_twin == True and identify_horizontal == False and identify_vertical == False )
    
    # 2. win Horizontally or Vertically :
    #    cells have identical row or has identical col
    win_not_diagonally = ( identify_horizontal == True or identify_vertical == True )
    
    winner_is_found = True if (win_diagonally == True or win_not_diagonally == True) else False
    return winner_is_found
    
#----------------------------------------------------------------------------------------------------
# OTHER
#----------------------------------------------------------------------------------------------------
  def __repr__(self):
    return self.print_out
