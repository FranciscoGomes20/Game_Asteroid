import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("data/ship.png")
        self.image = pygame.transform.scale(self.image, [90, 50])
        self.rect = pygame.Rect(50, 50, 50, 50)
        self.speed = 0
        self.acceleration = 0.1
        self.rect.x = 70
        self.rect.y = 190
    
    def update(self, *args):
        # Logica
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.speed -= self.acceleration
        elif keys[pygame.K_s]:
            self.speed += self.acceleration
        elif keys[pygame.K_a]:
            self.speed -= self.acceleration
        elif keys[pygame.K_d]:
            self.speed += self.acceleration
        else:
            self.speed *= 0.95

        self.rect.y += self.speed
        
        # Limite da tela
        if self.rect.top < 0:
            self.rect.top = 0
            self.speed = 0
        elif self.rect.bottom > 480:
            self.rect.bottom = 480
            self.speed = 0