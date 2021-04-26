import pygame
import random
from player import Player
from asteroid import Asteroid
from shot import Shot

ALTURA = 840    # Altura da tela/imgem background
LARGURA = 480   # Largura da tela/imagem background

# Inicio
pygame.init()
tela = pygame.display.set_mode([ALTURA, LARGURA])
pygame.display.set_caption("Primeiro Jogo!")

# Objeto grupo
objectGroup = pygame.sprite.Group()
asteroidGroup = pygame.sprite.Group()
shotGroup = pygame.sprite.Group()

# Backgroud
bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("data/grid_bg.png")
bg.image = pygame.transform.scale(bg.image, [ALTURA, LARGURA])
bg.rect = bg.image.get_rect()

# Player
player = Player(objectGroup)

# Musica
pygame.mixer.music.load("data/Retro Game.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

# Sound
shoot = pygame.mixer.Sound("data/Shoot.wav")
shoot.set_volume(0.2)

def main():
    somAtivado = True
    timer = 10
    gameLoop = True
    gameover = False
    clock = pygame.time.Clock()
    
    while gameLoop:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not gameover:
                    shoot.play()
                    newShot = Shot(objectGroup, shotGroup)
                    newShot.rect.center = player.rect.center
                
                if event.key == pygame.K_m:
                    if somAtivado:
                        pygame.mixer.music.stop()
                        somAtivado = False
                    else:
                        pygame.mixer.music.play(-1)
                        somAtivado = True
        
        # Tempo para a criação dos asteroides
        if not gameover:
            timer += 1
            if timer > 30:
                timer = 0
                if random.random() < 0.4:
                    newAsteroid = Asteroid(objectGroup, asteroidGroup)

            # Colisão dos asteroides
            collisions = pygame.sprite.spritecollide(player, asteroidGroup, False, pygame.sprite.collide_mask)
            if collisions:
                print("Game Over!")
                gameover = True
            
            # Shots
            hits = pygame.sprite.groupcollide(shotGroup, asteroidGroup, True, True, pygame.sprite.collide_mask)

            # Update
            objectGroup.update()
        
        # Draw
        objectGroup.draw(tela)
        pygame.display.update()

if __name__ == "__main__":
    main()