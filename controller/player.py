class Player :
  def __init__(self) :
    self.name  = None
    self.role  = None
    self.cells_selected = []
    self.score = 0

#-------------------------------------------------------------------------------------------
# Function for comp auto selected cells (based on game level)
#-------------------------------------------------------------------------------------------
  
  def easy_comp_cell(self) :
    #comp will select cell randomly
    pass
    
  def medium_comp_cell(self) :
    #comp will select cell with lowest winning chance
    pass
    
  def impossible_comp_cell(self) :
    #comp will select cell with highest winning chance
    pass
    
#-------------------------------------------------------------------------------------------
  
  def __repr__(self) :
    return f'Role : {self.role}\nScore : {self.score}\n Cells : {self.cells_selected}'