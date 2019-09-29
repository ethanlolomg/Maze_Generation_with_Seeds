import pygame

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# list that defines direction of DIRECTION variable
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

class Mazerunner:
    def __init__(self, maze):
        self.maze = maze
        self.sizex = maze.x
        self.sizey = maze.y
        self.x = maze.startX
        self.y = maze.startY
        self.xend = maze.endX
        self.yend = maze.endY
        self.screen = maze.screen
        self.color = (128, 128, 128)
        self.speed = 0
        self.lastMove = pygame.time.get_ticks()
        self.dir = RIGHT


    def draw(self):
        thisTick = pygame.time.get_ticks()
        if thisTick - self.lastMove > self.speed:
            #if not self.maze.grid[self.yend][self.xend]:
            # It's been self.speed milliseconds, move the snake
            if self.dir == RIGHT:
                if not self.maze.grid[self.y+1][self.x]:
                    self.dir = (self.dir + 1) % 4
                    self.y += 1
                elif not self.maze.grid[self.y][self.x+1]:
                    self.x += 1
                elif not self.maze.grid[self.y-1][self.x]:
                    self.dir = (self.dir + 3) % 4
                    self.y -= 1
                else:
                    self.dir = (self.dir + 1) % 4
            elif self.dir == LEFT:
                if not self.maze.grid[self.y-1][self.x]:
                    self.dir = (self.dir + 1) % 4
                    self.y -= 1
                elif not self.maze.grid[self.y][self.x-1]:
                    self.x -= 1
                elif not self.maze.grid[self.y+1][self.x]:
                    self.dir = (self.dir + 3) % 4
                    self.y += 1
                else:
                    self.dir = (self.dir + 1) % 4
                    #hereeeeee
            elif self.dir == UP:
                if not self.maze.grid[self.y][self.x+1]:
                    self.dir = (self.dir + 1) % 4
                    self.x += 1
                elif not self.maze.grid[self.y-1][self.x]:
                    self.y -= 1
                elif not self.maze.grid[self.y][self.x-1]:
                    self.dir = (self.dir + 3) % 4
                    self.x -= 1
                else:
                    self.dir = (self.dir + 1) % 4
            elif self.dir == DOWN:
                if not self.maze.grid[self.y][self.x-1]:
                    self.dir = (self.dir + 1) % 4
                    self.x -= 1
                elif not self.maze.grid[self.y+1][self.x]:
                    self.y += 1
                elif not self.maze.grid[self.y][self.x+1]:
                    self.dir = (self.dir + 3) % 4
                    self.x += 1
                else:
                    self.dir = (self.dir + 1) % 4

            if self.x == 1 and self.y == 1:
                return -1

            if self.x == self.xend and self.y == self.yend:
                return self.maze.seed

            self.lastMove = thisTick

        x = self.x * self.sizex
        y = self.y * self.sizey
        pygame.draw.rect(self.screen, self.color, (x, y, self.sizex, self.sizey) )
        return 0











    def draw2(self):
        thisTick = pygame.time.get_ticks()
        if thisTick - self.lastMove > self.speed:
            # It's been self.speed milliseconds, move the snake
            if self.dir == RIGHT:
                x = 0
                y = 1

            elif self.dir == LEFT:
                x = 0
                y = -1

            elif self.dir == UP:
                x = -1
                y = 0
            elif self.dir == DOWN:
                x = 1
                y = 0

            if not self.maze.grid[self.y + y][self.x + x]:
                self.dir = (self.dir + 1) % 4
                self.y += y + x
            elif not self.maze.grid[self.y + x][self.x + y]:
                self.x += y + x
            else:
                self.dir = (self.dir + 1) % 4

            self.lastMove = thisTick
