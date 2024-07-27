import pygame
from random import randint
window = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Shoter")
background = pygame.transform.scale(pygame.image.load("castle.webp"), (700, 500)) 
game = True
clock = pygame.time.Clock()
height = 500
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, speed, size_x,size_y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
player = GameSprite('rocket.png', 20, 408, 25,50,90)
enemies=[GameSprite('ufo.png', randint(0,640), -50, randint(1,1), 80, 50) for i in range(5)] 
bullets = []
pygame.mixer.init()
pygame.mixer.music.load('baby.mp3')
pygame.mixer.music.play()
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    window.blit(background,(0,0)  )

    player.draw()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        b = GameSprite('bullet.png', player.rect.centerx,player.rect.y, -1, 5, 20)    
        bullets.append(b)
        
    if keys[pygame.K_LEFT] and player.rect.x > 2:
        player.rect.x -= 1
    if keys[pygame.K_RIGHT] and player.rect.x < 645:
        player.rect.x += 1
    




    for bullet in bullets:
        bullet.draw()
        bullet.rect.y += bullet.speed
        if bullet.rect.y < -50:
            bullets.remove(bullet)
        for enemy in enemies:
            if bullet.rect.colliderect(enemy.rect):
                enemy.rect.y = -50
                enemy.rect.x = randint(0, 620)
                enemy.speed = randint(1, 1)

    
    
    
    for enemy in enemies:
        enemy.draw()
        enemy.rect.y += enemy.speed
        if enemy.rect.y > height:
            enemy.rect.y = -50
            enemy.rect.x = randint(0, 620)
            enemy.speed = randint(1, 1)


    print(len(bullets))

    pygame.display.update()
    clock.tick(144)
