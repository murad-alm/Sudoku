import pygame, sys
from settings import *
from button import *

class Sudoku:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE) 
        self.running = True
        self.grid = finishedBoard
        self.selectedCell = None
        self.mousePos = None
        self.state = "playing"
        self.finised = False
        self.cellChanged = False
        self.playingButtons = []
        self.idleButtons = []
        self.endGameButtons = []
        self.lockedCells = []
        self.wrongCells = []
        self.initButtons()
        self.setLockedCells()
        self.font = pygame.font.Font('freesansbold.ttf', cellSize // 2)


    def run(self):
        while(self.running):
            if (self.state == "playing"):
                self.playing_events()
                self.playing_update()
                self.playing_draw()

        pygame.quit()
        sys.exit()

#######  PLAYING STATE FUNCTIONS  #######

    def playing_events(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                self.running = False

            # mouse clicks
            if (event.type == pygame.MOUSEBUTTONDOWN):
                selectedCell = self.mouseClickOnGrid()
                if (selectedCell):
                    self.selectedCell = selectedCell
                else:
                    # not on board click
                    self.selectedCell = None

            # keyboard input
            if event.type == pygame.KEYDOWN:
                if (self.selectedCell != None) and (self.selectedCell not in self.lockedCells) and (self.isValidKey(event.unicode)):
                    self.grid[self.selectedCell[1]][self.selectedCell[0]] = int(event.unicode)
                    self.cellChanged = True

    
    def playing_update(self):
        self.mousePos = pygame.mouse.get_pos()
        for button in self.playingButtons:
            button.update(self.mousePos)

            if self.cellChanged:
                self.wrongCells = [] # reset the incorrect cells before every board check
                if self.allCellsFull():
                    self.validateBoard() # check if board is correct
                    if len(self.wrongCells) == 0:
                        print("CONGRATS!!!")
                        #TODO ENDGAME

    def playing_draw(self):
        self.window.fill(COLOR_WHITE)
        self.drawTitle(self.window)

        for button in self.playingButtons:
            button.draw(self.window)

        # TODO set an option to turn this off/on
        self.drawWrongCells(self.window, self.wrongCells)
        
        # draw user's selection color
        if (self.selectedCell):
            self.drawSelection(self.window, self.selectedCell)

        # draw the lockedCells in another color on top of the selection color (prevent highlighting the lockedCells)
        self.drawLockedCells(self.window, self.lockedCells)

        # draw numbers inside the cells after drawing the selection / lockedCells color
        self.drawNumbers(self.window)
        
        # draw the grid
        self.drawGrid(self.window)
        pygame.display.update()
        
        # finally reset the status
        self.cellChanged = False


#######  DRAW HELP FUNCTIONS  #######

    def drawTitle(self, window):
        # font = pygame.font.Font('freesansbold.ttf', 32) 
        text = self.font.render('SUDOKU', True, COLOR_WHITE, COLOR_BLACK) 
        textRect = text.get_rect()  
        textRect.center = (WIDTH / 2,  50) 
        window.blit(text, textRect) 


    def drawGrid(self, window):
        pygame.draw.rect(window, COLOR_BLACK, (gridPos[0], gridPos[1], WIDTH - 150, HEIGHT - 150), 3)
        for x in range(9):
            # vertical line
            pygame.draw.line(window, COLOR_BLACK, (gridPos[0] + (x * cellSize), gridPos[1]), (gridPos[0] + (x * cellSize), gridPos[1] + 450), 3 if (x % 3 == 0) else 1)
            # horizontal line
            pygame.draw.line(window, COLOR_BLACK, (gridPos[0], gridPos[1] + (x * cellSize)), (gridPos[0] + 450, gridPos[1] + (x * cellSize)), 3 if (x % 3 == 0) else 1)


    def drawSelection(self, window, pos):
        #re-calculate the given position (cell coordinates) in relation to the whole screen (not the grid only) then add the starting X&Y of the grid
        pygame.draw.rect(window, COLOR_GREEN, ((pos[0] * cellSize) + gridPos[0], (pos[1] * cellSize) + gridPos[1], cellSize, cellSize))


    def drawLockedCells(self, window, lockedCells):
        for cell in lockedCells:
            pygame.draw.rect(window, COLOR_LOCKED_CELLS, (cell[0] * cellSize + gridPos[0], cell[1] * cellSize + gridPos[1], cellSize, cellSize))

    def drawWrongCells(self, window, wrongCells):
        for cell in wrongCells:
            pygame.draw.rect(window, COLOR_RED, (cell[0] * cellSize + gridPos[0], cell[1] * cellSize + gridPos[1], cellSize, cellSize))

    def drawNumbers(self, window):
        for y, row in enumerate(self.grid):
            for x, number in enumerate(row):
                if (number != 0):
                    pos = [(x * cellSize) + gridPos[0], (y * cellSize) + gridPos[1]]
                    self.textToScreen(self.window, str(number), pos)


####### CHECK BOARD FUNCTIONS  #######

    def allCellsFull(self):
        for row in self.grid:
            for num in row:
                if num == 0:
                    return False
        return True

    def validateBoard(self):
        self.checkRows()
        self.checkColumns()
        self.check3x3()

    def checkRows(self):
        for y, row in enumerate(self.grid):
            possibleValues = [1,2,3,4,5,6,7,8,9]
            for x in range(9):
                if self.grid[y][x] in possibleValues:
                    possibleValues.remove(self.grid[y][x])
                else: # value of the cell doesn't exist in the possibleValues ==> it has been removed (we already had this value in the current row)
                    if [x, y] not in self.lockedCells: # original cells can't be wrong
                        self.wrongCells.append([x, y])

    def checkColumns(self):
        for x in range(9):
            possibleValues = [1,2,3,4,5,6,7,8,9]
            for y, row in enumerate(self.grid):
                if self.grid[y][x] in possibleValues:
                        possibleValues.remove(self.grid[y][x])
                else: 
                    if [x, y] not in self.lockedCells and [x, y] not in self.wrongCells: # don't add the same wrong cell twice to the wrongCells list
                        self.wrongCells.append([x, y])

    def check3x3(self):
        for xs in range(3):
            for ys in range(3):
                possibleValues = [1,2,3,4,5,6,7,8,9]
                for i in range(3):
                    for j in range(3):
                        x = xs * 3 + i
                        y = ys * 3 + j
                        if self.grid[y][x] in possibleValues:
                            possibleValues.remove(self.grid[y][x])
                        else:
                            if [x, y] not in self.lockedCells and [x, y] not in self.wrongCells:
                                self.wrongCells.append([x, y])



#######  OTHER FUNCTIONS  #######        
    
    def textToScreen(self, window, text, pos):
        font = self.font.render(text, True, COLOR_BLACK)
        fontWidth = font.get_width()
        fontHeight = font.get_height()
        pos[0] += (cellSize - fontWidth) // 2
        pos[1] += (cellSize - fontHeight) // 2
        window.blit(font, pos)

    def initButtons(self):
        self.playingButtons.append(Button(gridPos[0], (HEIGHT - (BUTTON_HEIGHT + 1)), BUTTON_WIDTH, BUTTON_HEIGHT))
        self.playingButtons.append(Button(gridPos[0] + (450 - BUTTON_WIDTH), (HEIGHT - (BUTTON_HEIGHT + 1)), BUTTON_WIDTH, BUTTON_HEIGHT))

    def mouseClickOnGrid(self):
        # if the click is out of the grid horizontally
        if (self.mousePos[0] < gridPos[0] or self.mousePos[0] > gridPos[0] + gridSize):
            return False
        # if the click is out of the grid vertically
        if (self.mousePos[1] < gridPos[1] or self.mousePos[1] > gridPos[1] + gridSize):
            return False
        else:
            # return the coordinates of the clicked cell in the grid
            # first calculate the mouse position in relation to the grid position (starting by the top left corner)
            # then divide by cell size to get the coordinates of the clicked cell
            return [(self.mousePos[0] - gridPos[0]) // cellSize, (self.mousePos[1] - gridPos[1]) // cellSize]

    def setLockedCells(self):
        # loop through the grid and set all cells which has a non-zero value as 'LockedCells'
        # the lockedCells will be rendered in another color and will be locked so the user can't modify their original value
        for y, row in enumerate(self.grid):
            for x, num in enumerate(row):
                if (num != 0):
                    self.lockedCells.append([x, y])

    def isValidKey(self, key):
        try:
            int(key)
            if int(key) != 0:
                return True
        except:
            return False