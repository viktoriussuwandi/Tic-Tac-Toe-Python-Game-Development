class Player :
  def __init__(self) :
    self.role  = None
    self.score = 0
  
  def __repr__(self) :
    return f'Role : {self.role}\nScore : {self.score}'