import pygame, sys
from settings import *
from button import *

class Sudoku:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE) 
        self.running = True
        self.grid = testBoard2
        self.selectedCell = None
        self.mousePos = None
        self.state = "playing"
        self.playingButtons = []
        self.idleButtons = []
        self.endGameButtons = []
        self.lockedCells = []
        self.load()
        self.initButtons()
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

            if (event.type == pygame.MOUSEBUTTONDOWN):
                selectedCell = self.mouseClickOnGrid()
                if (selectedCell):
                    self.selectedCell = selectedCell
                else:
                    print('not on board')
                    self.selectedCell = None

    
    def playing_update(self):
        self.mousePos = pygame.mouse.get_pos()
        for button in self.playingButtons:
            button.update(self.mousePos)


    def playing_draw(self):
        self.window.fill(COLOR_WHITE)
        self.drawTitle(self.window)

        for button in self.playingButtons:
            button.draw(self.window)
        
        # draw user's selection color
        if (self.selectedCell):
            self.drawSelection(self.window, self.selectedCell)

        # draw the lockedCells in another color on top of the selection color (prevent highlighting the lockedCells)
        self.drawLockedCells(self.window, self.lockedCells)

        # draw numbers inside the cells after drawing the selection / lockedCells color
        self.drawNumbers(self.window)
        
        # finally draw the grid
        self.drawGrid(self.window)
        pygame.display.update()


#######  DRAW HELPING FUNCTIONS  #######

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

    def drawNumbers(self, window):
        for y, row in enumerate(self.grid):
            for x, number in enumerate(row):
                if (number != 0):
                    pos = [(x * cellSize) + gridPos[0], (y * cellSize) + gridPos[1]]
                    self.textToScreen(self.window, str(number), pos)

##########################################################
    
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
            return ((self.mousePos[0] - gridPos[0]) // cellSize, (self.mousePos[1] - gridPos[1]) // cellSize)


    def load(self):
        # loop through the grid and set all cells which has a non-zero value as 'LockedCells'
        # the lockedCells will be rendered in another color and will be locked so the user can't modify their original value
        
        for y, row in enumerate(self.grid):
            for x, num in enumerate(row):
                if (num != 0):
                    self.lockedCells.append([x, y])
        print(self.lockedCells)