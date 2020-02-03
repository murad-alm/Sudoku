import pygame, sys
from settings import *

class Sudoku:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.grid = testBoard
        pygame.display.set_caption(WINDOW_TITLE) 


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

    
    def update(self):
        pass


    def draw(self):
        self.window.fill(WHITE)
        self.drawTitle(self.window)
        self.drawGrid(self.window)
        pygame.display.update()


    def drawTitle(self, window):
        font = pygame.font.Font('freesansbold.ttf', 32) 
        text = font.render('SUDOKU', True, WHITE, BLACK) 
        textRect = text.get_rect()  
        # set the center of the rectangular object. 
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


    