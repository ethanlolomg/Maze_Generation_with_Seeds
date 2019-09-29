import pygame
import random
import time

class Maze:
    def __init__(self, screen, sizeX=10, sizeY=10, seed = None):
        if seed is None:
            self.seed = int(time.time())
        else:
            self.seed = seed


        random.seed(self.seed)
        self.width = sizeX
        self.height = sizeY
        self.grid = []
        self.startX = 1
        self.startY = 1
        self.endX = sizeX - 2
        self.endY = sizeY - 2
        # Used for drawing the maze
        self.x = 10
        self.y = 10
        self.screen = screen

        for y in range(sizeY):
            row = []
            for x in range(sizeX):
                row.append(True)
            self.grid.append(row)


        for i in range(1, sizeY, 2):
            for l in range(1, sizeX, 2):
                self.grid[i][l] = False

        for y in range(1, self.height / 2, 2):
            for x in range(1, self.width / 2, 2):
                wall = random.randrange(0, 2)
                if wall == 0:
                    self.grid[y][x + 1] = False
                elif wall == 1:
                    self.grid[y + 1][x] = False

        for y in range(self.height - 2, self.height / 2, -2):
            for x in range(self.width - 2, self.width / 2, -2):
                wall = random.randrange(0, 2)
                if wall == 0:
                    self.grid[y][x - 1] = False
                elif wall == 1:
                    self.grid[y - 1][x] = False

        for y in range(1, self.height / 2, 2):
            for x in range(self.width - 2, self.width / 2, -2):
                wall = random.randrange(0, 2)
                if wall == 0:
                    self.grid[y][x - 1] = False
                elif wall == 1:
                    self.grid[y + 1][x] = False

        for y in range(self.height - 2, self.height / 2, -2):
            for x in range(1, self.width / 2, 2):
                wall = random.randrange(0, 2)
                if wall == 0:
                    self.grid[y][x + 1] = False
                elif wall == 1:
                    self.grid[y - 1][x] = False

        '''
        self.celly = 2
        self.cellx = 1
        self.wall = 0
        for z in range(sizeY / 4 - 1):
            for j in range(sizeX / 2 - 1):
                self.wall = random.randrange(0, 2)
                if self.wall == 0:
                    self.grid[self.celly][self.cellx + 1] = " "
                if self.wall == 1:
                    self.grid[self.celly + 2][self.cellx] = " "
                self.cellx = self.cellx + 2
            self.cellx = 1
            self.celly = self.celly + 4

        self.celly = 40
        self.cellx = 20
        self.wall = 0
        for z in range(6):
            for j in range(18):
                self.wall = random.randrange(0, 2)
                if self.wall == 0:
                    self.grid[self.celly][self.cellx - 1] = " "
                if self.wall == 1:
                    self.grid[self.celly - 2][self.cellx] = " "
                self.cellx = self.cellx - 2
            self.cellx = sizeX - 1
            self.celly = self.celly - 4
        '''
        '''
        self.celly = 2
        self.cellx = 1
        self.wall = 0
        for z in range(int(sizeY / 2 - 1)):
            for j in range(int(sizeX / 2 - 1)):
                self.wall = random.randrange(0, 2)
                if self.wall == 0:
                    self.grid[self.celly][self.cellx + 1] = " "
                if self.wall == 1:
                    self.grid[self.celly + 2][self.cellx] = " "
                self.cellx = self.cellx + 2
            self.cellx = 1
            self.celly = self.celly + 4

        for n in range(int(sizeX / 2 - 1)):
            self.wall = random.randrange(0, 2)
            if self.wall == 0:
                self.grid[self.celly][self.cellx + 1] = " "
            if self.wall == 1:
                self.grid[self.celly - 2][self.cellx] = " "
            self.cellx = self.cellx + 2

        self.celly = 2
        self.cellx = sizeX - 2
        self.wall = 0
        for n in range(int(sizeY / 2 - 1)):
            self.wall = random.randrange(0, 2)
            if self.wall == 0:
                self.grid[self.celly][self.cellx - 1] = " "
            if self.wall == 1:
                self.grid[self.celly - 2][self.cellx] = " "
            self.celly = self.celly + 4

        self.celly = 2
        self.cellx = 1
        self.wall = 0
        for n in range(int(sizeY / 2 - 1)):
            self.wall = random.randrange(0, 2)
            if self.wall == 0:
                self.grid[self.celly][self.cellx + 1] = " "
            if self.wall == 1:
                self.grid[self.celly - 2][self.cellx] = " "
            self.celly = self.celly + 2
            self.cellx = self.cellx + 4
        '''
        # Here, we open a path from start (0,0) to end (Height/Width)
        # set the [0] to x and y, and than randomly add one to one on them until it reach the size maximum
    def draw (self):
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x]:
                    pygame.draw.rect(self.screen, (0,180,0), (x * self.x, y * self.y, self.x, self.y))
                if x == self.startX and y == self.startY:
                    pygame.draw.rect(self.screen, (255, 0, 0), (x * self.x, y * self.y, self.x, self.y))
                if x == self.endX and y == self.endY:
                    pygame.draw.rect(self.screen, (0, 0, 255), (x * self.x, y * self.y, self.x, self.y))

    def __str__(self):
        output = ""
        for j in self.grid:
            for z in j:
                if z:
                    output += "8"
                else:
                    output += " "
            output += '\n'

        return output


















'''
class Maze:
    def __init__(self, sizeX = 10, sizeY = 10):
        self.width = sizeX
        self.height = sizeY
        self.grid = []
        self.celly = 2
        self.cellx = 1
        for y in range(sizeY):
            #self.y = self.y + 2
            row = []
            for x in range(sizeX):
                #self.x = self.x + 2
                row.append(chr(219))
            self.grid.append(row)
            #self.grid.append('\n')

        for i in range(sizeY/2):
            for l in range (sizeX/2):
                self.grid[self.celly][self.cellx]= " "
                self.cellx = self.cellx+2
            self.cellx = 1
            self.celly = self.celly+2

        
        self.celly = 0
        self.cellx = 0
        self.wall = 0
        for z in range(int(sizeY / 2)):
            for j in range(int(sizeX / 2)):
                self.wall = random.randrange(0, 2)
                if self.wall == 0:
                    self.grid[self.celly][self.cellx + 1] = " "
                if self.wall == 1:
                    self.grid[self.celly + 1][self.cellx] = " "
                self.cellx = self.cellx + 2
            self.cellx = 1
            self.celly = self.celly + 2
        
        self.celly = 2
        self.cellx = 1
        self.wall = 0
        for z in range (sizeY/4 -1):
            for j in range (sizeX/4-1):
                self.wall = random.randrange(0, 2)
                if self.wall == 0:
                    self.grid[self.celly][self.cellx + 1] = " "
                if self.wall == 1:
                    self.grid[self.celly + 2][self.cellx] = " "
                self.cellx = self.cellx + 2
            self.cellx = 1
            self.celly = self.celly + 4

        self.celly = sizeY-1
        self.cellx = sizeX-1
        self.wall = 0
        for z in range(sizeY / 4 -1):
            for j in range(sizeX /4 -1):
                self.wall = random.randrange(0, 2)
                if self.wall == 0:
                    self.grid[self.celly][self.cellx + 1] = " "
                if self.wall == 1:
                    self.grid[self.celly + 2][self.cellx] = " "
                self.cellx = self.cellx - 2
            self.cellx = sizeX
            self.celly = self.celly - 4



        for n in range(sizeX / 2 - 1):
            self.wall = random.randrange(0, 2)
            if self.wall == 0:
                self.grid[self.celly][self.cellx + 1] = " "
            self.cellx = self.cellx + 2

        #self.grid[self.celly][self.cellx + 1] = " "
        #self.grid[2][1]= "s"


        # Here, we open a path from start (0,0) to end (Height/Width)
        #set the [0] to x and y, and than randomly add one to one on them until it reach the size maximum


    def __str__(self):
        output = ""
        for j in self.grid:
            for z in j:
                output += str(z)
            output += '\n'
        
        return output
'''

