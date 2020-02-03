WIDTH = 600
HEIGHT = 600
WINDOW_TITLE = 'Sudoku Game with Python'

#colors:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255) 



testBoard = [[0 for x in range(9)] for x in range(9)]

#positions and sizes
gridPos = (75, 100)
cellSize = 50
gridSize = cellSize * 9
