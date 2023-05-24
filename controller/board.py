import math

class Board :
  def __init__(self, total_cells = None) :
    self.total_square = total_cells if total_cells is not None else None
    self.row       = None
    self.col       = None
    self.all_cells = [] 
    self.starting_board = {}
    self.create_board()

  def create_board(self) :
    if self.total_square is not None :
      self.row = int(math.sqrt(self.total_square))
      self.col = self.row
      self.all_cells = [ [row,col] for row in range(self.row) for col in range(self.col) ]
      self.starting_board = { "row": self.row, "col" : self.col }
  
  def update_board(self) :
    return self.starting_board