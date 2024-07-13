import pygame
window = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Shoter")
background = pygame.transform.scale(pygame.image.load("castle.webp"), (700, 500)) 
game = True
clock = pygame.time.Clock()

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
player = GameSprite('rocket.png', 20, 408, 4,50,90)

pygame.mixer.init()
pygame.mixer.music.load('baby.mp3')
pygame.mixer.music.play()
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.rect.x > 2:
        player.rect.x -= 1
    if keys[pygame.K_RIGHT] and player.rect.x < 645:
        player.rect.x += 1
    

    

    
    window.blit(background,(0,0)  )
    player.draw()
    pygame.display.update()
    clock.tick()