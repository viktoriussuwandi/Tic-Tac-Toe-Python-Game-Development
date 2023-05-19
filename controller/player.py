class Player :
  def __init__(self, role=None) :
    self.mark = "X" if role == "X" else "O"
    self.score = 0
  
  def __repr__(self): 
    return self.mark