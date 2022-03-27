class Board:
  def __init__(self, size):
    self.size = size
    self.grid = [ [ None for j in range(size) ] for i in range(size) ]
    for i in range (size):
      for j in range (size):
        self.grid[i][j] = str(i) + str(j)


  def display(self):
    for i in range (self.size):
      print(self.grid[i])

  def reset(self):
    for i in range (self.size):
      self.grid[0][i] = "O"
      for j in range (1, self.size - 1):
        self.grid[j][i] = " "
      self.grid[self.size - 1][i] = "X"
b = Board(3)
b.reset()
b.display()
