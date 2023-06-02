class Player :
  def __init__(self) :
    self.name  = None
    self.role  = None
    self.cells_selected = []
    self.score = 0

  def easy_comp_cell(self) :
    pass
    
  def medium_comp_cell(self) :
    pass
    
  def impossible_comp_cell(self) :
    pass
    
  def __repr__(self) :
    return f'Role : {self.role}\nScore : {self.score}\n Cells : {self.cells_selected}'