#2020 Levi D. Smith - levidsmith.com
#Enemy added, which moves back and forth horizontally
import pygame

class Ship:
    x = 640
    y = 600
    w = 64
    h = 64
    
    vel_x = 0
    vel_y = 0
    
    def draw(self, display):
        #Draw Ship
        c = (0, 255, 255)
        pygame.draw.rect(display, c, (self.x, self.y, self.w, self.h))
        
    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y
        
        if (self.x < 0):
            self.x = 0
        elif (self.x > 1280 - self.w):
            self.x = 1280 - self.w
        
        if (self.y < 0):
            self.y = 0
        elif (self.y > 720 - self.h):
            self.y = 720 - self.h
        
    def moveLeft(self):
        self.vel_x = -5
    
    def moveRight(self):
        self.vel_x = 5
    
    def moveUp(self):
        self.vel_y = -5
    
    def moveDown(self):
        self.vel_y = 5

    def stopMovingLeft(self):
        if (self.vel_x < 0):
            self.vel_x = 0

    def stopMovingRight(self):
        if (self.vel_x > 0):
            self.vel_x = 0

    def stopMovingUp(self):
        if (self.vel_y < 0):
            self.vel_y = 0

    def stopMovingDown(self):
        if (self.vel_y > 0):
            self.vel_y = 0


class Enemy:
    x = 0
    y = 0
    w = 64
    h = 64
    
    vel_x = 2
    iCountdown = 120
    
    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y
    
    def draw(self, display):
        c = (0, 255, 0)
        pygame.draw.rect(display, c, (self.x, self.y, self.w, self.h))
        
    def update(self):
        self.x += self.vel_x
        self.iCountdown -= 1
        if (self.iCountdown <= 0):
            self.vel_x *= -1
            self.iCountdown = 120
            


enemy = Enemy(200, 200)
ship = Ship()


def update():
    ship.update()
    enemy.update()


def draw(display):
    c = (0, 0, 0)
    display.fill(c)
    enemy.draw(display)
    ship.draw(display)



def main():
    pygame.init()
    display = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Test Window')

    clock = pygame.time.Clock()

    keepLooping = True
    while keepLooping:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepLooping = false
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                    ship.moveLeft()
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                    ship.moveRight()
                elif (event.key == pygame.K_UP or event.key == pygame.K_w):
                    ship.moveUp()
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                    ship.moveDown()
                elif (event.key == pygame.K_ESCAPE or event.key == pygame.K_q):
                    keepLooping = False
            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                    ship.stopMovingLeft()
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                    ship.stopMovingRight()
                elif (event.key == pygame.K_UP or event.key == pygame.K_w):
                    ship.stopMovingUp()
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                    ship.stopMovingDown()


        update()
        draw(display)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()
    
main()

