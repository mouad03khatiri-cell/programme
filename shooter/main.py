from game import Game
import pygame # type:ignore
import math
pygame.init()


clock = pygame.time.Clock()
FPS = 1000


pygame.display.set_caption("Comet Fall Game")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load("html/python/assets/bg.jpg")

banner = pygame.image.load("html/python/assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

play_button = pygame.image.load("html/python/assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

game = Game()

running = True

while running:    
    screen.blit(background, (0, -200))
    
    if game.is_playing:
        game.update(screen)
        
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            
            
            if event.key == pygame.K_SPACE:
                if game.is_playing == True:
                    game.player.launch_projectile()
                else:
                    game.start()
                    game.sound_manager.play('click')
            
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()
                game.sound_manager.play('click')
             
    clock.tick(FPS)
           
pygame.quit()