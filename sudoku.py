import pygame, sys
from settings import *

class Sudoku:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.grid = testBoard
        pygame.display.set_caption(WINDOW_TITLE) 
        self.selectedCell = None
        self.mousePos = None


    def run(self):
        while(self.running):
            self.events()
            self.update()
            self.draw()

        pygame.quit()
        sys.exit()


    def events(self):
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

    
    def update(self):
        self.mousePos = pygame.mouse.get_pos()


    def draw(self):
        self.window.fill(WHITE)
        self.drawTitle(self.window)
        
        if (self.selectedCell):
            self.drawSelection(self.window, self.selectedCell)
            
        self.drawGrid(self.window)
        pygame.display.update()


    def drawTitle(self, window):
        font = pygame.font.Font('freesansbold.ttf', 32) 
        text = font.render('SUDOKU', True, WHITE, BLACK) 
        textRect = text.get_rect()  
        textRect.center = (WIDTH / 2,  50) 
        
        self.window.blit(text, textRect) 



    def drawGrid(self, window):
        pygame.draw.rect(window, BLACK, (gridPos[0], gridPos[1], WIDTH - 150, HEIGHT - 150), 2)
        for x in range(9):
            if x % 3 == 0:
                # vertical line
                pygame.draw.line(window, BLACK, (gridPos[0] + (x * cellSize), gridPos[1]), (gridPos[0] + (x * cellSize), gridPos[1] + 450), 2)
                # horizontal line
                pygame.draw.line(window, BLACK, (gridPos[0], gridPos[1] + (x * cellSize)), (gridPos[0] + 450, gridPos[1] + (x * cellSize)), 2)
            else:
                # vertical line
                pygame.draw.line(window, BLACK, (gridPos[0] + (x * cellSize), gridPos[1]), (gridPos[0] + (x * cellSize), gridPos[1] + 450))
                # horizontal line
                pygame.draw.line(window, BLACK, (gridPos[0], gridPos[1] + (x * cellSize)), (gridPos[0] + 450, gridPos[1] + (x * cellSize)))


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
            # then devide by cell size to get the coordinates of the clicked cell
            return ((self.mousePos[0] - gridPos[0]) // cellSize, (self.mousePos[1] - gridPos[1]) // cellSize)

    def drawSelection(self, window, pos):
        #re-calculate the given position (cell coordinates) in relation to the whole screen (not the grid only) then add the starting X&Y of the grid
        pygame.draw.rect(window, GREEN, ((pos[0] * cellSize) + gridPos[0], (pos[1] * cellSize) + gridPos[1], cellSize, cellSize))