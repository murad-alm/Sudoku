WIDTH = 600
HEIGHT = 600
WINDOW_TITLE = 'Sudoku Game with Python'

#colors:
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (13, 242, 201)
COLOR_BLUE = (78, 197, 241)
COLOR_GRAY = (57, 81, 70)
COLOR_RED = (242, 90, 107)
COLOR_LOCKED_CELLS = (155, 151, 156)


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

finishedBoard = [[5,3,4,6,7,8,9,1,2],
                 [6,7,2,1,9,5,3,4,8],
                 [1,9,8,3,4,2,5,6,7],
                 [8,5,9,7,6,1,4,2,3],
                 [4,2,6,8,5,3,7,9,1],
                 [7,1,3,9,2,4,8,5,6],
                 [9,6,1,5,3,7,2,8,4],
                 [2,8,7,4,1,9,6,3,5],
                 [3,4,5,2,8,6,1,7,0]
                ]



#positions and sizes
gridPos = (75, 100)
cellSize = 50
gridSize = cellSize * 9

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 40

