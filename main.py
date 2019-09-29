import pygame
import random
from Maze import Maze
from Mazerunner import Mazerunner

goodmazeseed = [1566759841, 1566759848, 1567331211, 1567331247, 1567331278, 1567331317]
mazeseed = [None]
mazeseed = goodmazeseed
seednum = 0
pygame.init()

#mymazerunner = Mazerunner()

black = (0,0,0)
grey = (50, 50, 50)
green = (0, 200, 0)
red = (200, 0, 0)
yellow = (255, 255, 0)

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Random Maze')
mymaze = Maze(screen, 41, 21, seed = mazeseed[seednum])
runner = Mazerunner(mymaze)


print(mymaze)

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    screen.fill(black)
    mymaze.draw()
    if runner is not None:
        r = runner.draw()
    if r == -1:
        seednum += 1
        seednum %= len(mazeseed)
        mymaze = Maze(screen, 41, 21, seed = mazeseed[seednum])
        runner = Mazerunner(mymaze)
    if r > 0:
        seednum += 1
        seednum %= len(mazeseed)
        mymaze = Maze(screen, 41, 21, seed=mazeseed[seednum])
        runner = Mazerunner(mymaze)
        goodmazeseed.append(r)
        print (r)
    pygame.display.flip()

screen.fill(grey)
pygame.quit()
#print(mymaze)