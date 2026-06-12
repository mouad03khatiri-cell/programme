import pygame # type:ignore
import random

class Comet(pygame.sprite.Sprite):
    
    def __init__(self, comet_event):
        super().__init__()
        self.comet_event = comet_event
        self.image = pygame.image.load("html/python/assets/comet.png")
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.velocity = random.randint(6, 10)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 80) 
    def remove(self):
        self.comet_event.all_comets.remove(self)
        # joueur le son
        self.comet_event.game.sound_manager.play('meteorite')
        if len(self.comet_event.all_comets) == 0:
            print("Levenement est fini")
            self.comet_event.reset_percent()
            self.comet_event.game.start()
        
    def fall(self):
        self.rect.y += self.velocity
        
        if self.rect.y >= 500:
            print("Sol")
            self.remove()
            
            if len(self.comet_event.all_comets) == 0:
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False
            
        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_players
        ):
            print("Joueur Touche")
            self.remove()
       
            self.comet_event.game.player.damage(20)