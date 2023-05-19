class Player :
  def __init__(self, role=None) :
    self.mark = "X" if role == "human" else "O"
    self.score = 0
