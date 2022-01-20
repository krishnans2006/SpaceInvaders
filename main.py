import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)
pygame.mixer.music.load("background.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
starttime = time.time()

font = pygame.font.Font("Font.ttf", 32)
font2 = pygame.font.Font("Font.ttf", 100)

score = 0


def showscore(x=10, y=10, color=(255, 255, 255)):
    scoretext = font.render("Score: {0}".format(score), True, color)
    screen.blit(scoretext, (x, y))


playerX = 368
playerY = 500
playerXchange = 0


def player(x, y):
    screen.blit(pygame.image.load("player.png"), (x, y))


invadermove = random.choice([0.4, -0.4])
multiplied = True


class Invader:
    def __init__(self):
        self.x = random.randint(10, 726)
        self.y = random.randint(10, 110)
        self.xchange = invadermove
        self.xmultiplier = 0.4
        self.image = pygame.image.load("invader.png")

    def display(self):
        screen.blit(self.image, (self.x, self.y))

    def randomize(self):
        self.x = random.randint(10, 726)
        self.y = random.randint(10, 110)


invader1 = Invader()
invader2 = Invader()
while abs(invader1.x - invader2.x) < 74:
    invader2.randomize()

bullet1X = None
bullet1Y = None
"""
bullet2X = None
bullet2Y = None
bullet3X = None
bullet3Y = None
bullet4X = None
bullet4Y = None
bullet5X = None
bullet5Y = None
"""


def bullet(x, y):
    screen.blit(pygame.image.load("bullet.png"), (x, y))


running = True
"""
bullet2 = False
bullet3 = False
bullet4 = False
bullet5 = False
"""


def checkCollision():
    if bullet1X is not None:
        if -7 < bullet1X - invader1.x < 47 and 0 < bullet1Y - invader1.y < 40:
            return 1
        elif -7 < bullet1X - invader2.x < 47 and 0 < bullet1Y - invader2.y < 40:
            return 2
        else:
            return 0
    else:
        return -1


while running:
    screen.fill((0, 25, 40))
    if time.time() - starttime > 20:
        pygame.mixer.music.rewind()
        pygame.mixer.music.play(-1)
        starttime = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXchange = -0.5
            if event.key == pygame.K_RIGHT:
                playerXchange = 0.5
            if event.key == pygame.K_SPACE:
                if bullet1X is None:
                    bulletsound = pygame.mixer.Sound("laser.wav")
                    bulletsound.play()
                    bullet1X = playerX + 20
                    bullet1Y = 484
                """
                elif bullet2X is None:
                    bullet2X = playerX + 20
                    bullet2Y = 484
                elif bullet3X is None:
                    bullet3X = playerX + 20
                    bullet3Y = 484
                elif bullet4X is None:
                    bullet4X = playerX + 20
                    bullet4Y = 484
                elif bullet5X is None:
                    bullet5X = playerX + 20
                    bullet5Y = 484
                """
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXchange = 0
    if playerX > 726 and playerXchange > 0:
        playerXchange = 0
    if playerX < 10 and playerXchange < 0:
        playerXchange = 0
    playerX += playerXchange
    player(playerX, playerY)
    if score % 20 == 0 and not multiplied:
        invader1.xmultiplier += 0.1
        invader2.xmultiplier += 0.1
        multiplied = True
    invader1.display()
    invader2.display()
    if invader1.x > 726:
        invader1.xchange = invader1.xmultiplier * -1
    elif invader1.x < 10:
        invader1.xchange = invader1.xmultiplier
    if invader2.x > 726:
        invader2.xchange = invader2.xmultiplier * -1
    elif invader2.x < 10:
        invader2.xchange = invader1.xmultiplier
    invader1.x += invader1.xchange
    invader1.y += 0.05
    invader2.x += invader2.xchange
    invader2.y += 0.05
    if bullet1Y is not None and bullet1Y < 10:
        bullet1X = None
        bullet1Y = None
    """
    if bullet2Y is not None and bullet2Y < 10:
        bullet2X = None
        bullet2Y = None
    if bullet3Y is not None and bullet3Y < 10:
        bullet3X = None
        bullet3Y = None
    if bullet4Y is not None and bullet4Y < 10:
        bullet4X = None
        bullet4Y = None
    if bullet5Y is not None and bullet5Y < 10:
        bullet5X = None
        bullet5Y = None
    """
    if bullet1X is not None:
        bullet(bullet1X, bullet1Y)
        bullet1Y -= 1
    """
    if bullet2X is not None:
        bullet(bullet2X, bullet2Y)
        bullet2Y -= 1
    if bullet3X is not None:
        bullet(bullet3X, bullet3Y)
        bullet3Y -= 1
    if bullet4X is not None:
        bullet(bullet4X, bullet4Y)
        bullet4Y -= 1
    if bullet5X is not None:
        bullet(bullet5X, bullet5Y)
        bullet5Y -= 1
    """
    showscore()
    collision = checkCollision()
    if collision == 1:
        bulletsound = pygame.mixer.Sound("explosion.wav")
        bulletsound.play()
        screen.blit(pygame.image.load("explosion.png"), (invader1.x, invader1.y))
        pygame.display.update()
        time.sleep(0.5)
        invader1.randomize()
        bullet1X = None
        bullet1Y = None
        score += 1
        multiplied = False
    elif collision == 2:
        screen.blit(pygame.image.load("explosion.png"), (invader2.x, invader2.y))
        bulletsound = pygame.mixer.Sound("explosion.wav")
        bulletsound.play()
        pygame.display.update()
        time.sleep(0.5)
        invader2.randomize()
        bullet1X = None
        bullet1Y = None
        score += 1
        multiplied = False
    if invader1.y > 436 or invader2.y > 436:
        for i in range(324):
            if invader1.y > 436:
                invader1.y += 0.5
                invader1.display()
            elif  invader2.y > 436:
                invader2.y += 0.5
                invader2.display()
            pygame.display.update()
        screen.fill((200, 200, 200))
        screen.blit(pygame.image.load("gameover.png"), (144, 44))
        showscore(color=(0, 0, 0))
        pygame.display.update()
        pygame.mixer.music.fadeout(1000)
        time.sleep(2.5)
        screen.fill((200, 200, 200))
        screen.blit(font2.render("Final Score:", True, (0, 0, 0)), (10, 100))
        screen.blit(font2.render("{0}".format(score), True, (0, 0, 0)), (10, 250))
        screen.blit(font2.render("Press q to quit", True, (0, 0, 0)), (10, 400))
        pygame.display.update()
        end = False
        while not end:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        end = True
                if event.type == pygame.QUIT:
                    end = True
        running = False
    pygame.display.update()
