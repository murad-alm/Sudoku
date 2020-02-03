WIDTH = 600
HEIGHT = 600
WINDOW_TITLE = 'Sudoku Game with Python'

#colors:
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (13, 242, 201)
COLOR_BLUE = (78, 197, 241)
COLOR_GRAY = (57, 81, 70)


testBoard = [[0 for x in range(9)] for x in range(9)]

testBoard2 = [[0,6,0,2,0,0,8,3,1],
              [0,0,0,0,8,4,0,0,0],
              [0,0,7,6,0,3,0,4,9],
              [0,4,6,8,0,2,1,0,0],
              [0,0,0,3,9,6,0,0,0],
              [1,2,0,7,0,5,0,0,6],
              [7,3,0,0,0,1,0,2,0],
              [8,1,5,0,2,9,7,0,0],
              [0,0,0,0,7,0,0,1,5]]



#positions and sizes
gridPos = (75, 100)
cellSize = 50
gridSize = cellSize * 9

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 40

