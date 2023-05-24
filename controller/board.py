import math

class Board :
  def __init__(self, total_cells = None) :
    self.total_square = total_cells if total_cells is not None else None
    self.row       = None
    self.col       = None
    self.all_cells = []
    self.starting_board = {}
    self.create_board()
    self.cell_owners = [ None for i in self.all_cells ]
    self.print_out   = ''
    
  def create_board(self) :
    if self.total_square is not None :
      self.row = int(math.sqrt(self.total_square))
      self.col = self.row
      self.all_cells = [ [row,col] for row in range(self.row) for col in range(self.col) ]
      self.starting_board = { "row": self.row, "col" : self.col }

  def update_board(
    self, player_role = None, comp_role = None, is_player_selecting = False, 
    is_comp_selecting = False, player_cells = None, comp_cells = None ) :
    all_cells    = self.all_cells
    for i in range(len(all_cells)) :
      # Check if cell own by player     
      if is_player_selecting :
        for j in range(len(player_cells)) :
          player_own = self.cell_owners[i] is None and all_cells[i] == player_cells[j]
          self.cell_owners[i] = player_role if player_own else self.cell_owners[i]
          
      # Check if cell own by Comp
      if is_comp_selecting :
        for j in range(len(comp_cells)) :
          comp_own = self.cell_owners[i] is None and all_cells[i] == comp_cells[j]
          self.cell_owners[i] = comp_role if comp_own else self.cell_owners[i]

    self.print_out = ''
    for o in range(len(self.cell_owners)) :
      first_col = o % self.row == 0
      if     o == 0 : self.print_out +=f'     {str(self.cell_owners[o])}'
      elif   first_col : self.print_out +=f'\n     {str(self.cell_owners[o])}'
      else : self.print_out += f' {str(self.cell_owners[o])}'
  
  def __repr__(self) :
    return self.print_out
    
  