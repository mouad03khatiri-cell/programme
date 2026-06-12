import pygame
import random
import animation


# cree une classe qui va gerer la notion de monstre sur notre jeu
class Monster(animation.AnimateSprite):
    
    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1200 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.loot_amount = 1
        self.velocity = random.randint(2, 4)
        self.start_animaion()
        
    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, speed)
        
    def set_loot_amount(self, amount):
        self.loot_amount = amount
        
    def damage(self, amount):
        # Infliger les degats
        self.health -= amount
        
        # verifier si son nouveau nombre de points de vie est inferieur ou egal a zero
        if self.health <= 0:
            # Reapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health
            self.velocity = random.randint(1, self.default_speed)
            # ajoter le nombre de points
            self.game.add_score(self.loot_amount)
            
            # si la barre d'evenement est charge au maximaume
            if self.game.comet_event.is_full_loaded():
                # le retirer du jeu
                self.game.all_monsters.remove(self)
                
                # appel de la methode pour essayer de dechlancer la pluie de cometes
                self.game.comet_event.attempt_fall()
                
    def update_animation(self):
        self.animate(loop=True)
        
    def update_health_bar(self, surface):
        # dessiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y -20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y -20, self.health, 5])

        
    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision avec le joueur
        else:
            # Ifliger des degats (au joueur) Ainsi qu'a le monstre
            self.game.player.damage(self.attack)
            
# definir une class pour la momie
class Mummy(Monster):
    
    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(4)
        self.set_loot_amount(1)
        
# definir une classe pour l'aliene
class Alien(Monster):
    
    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 130)
        self.health = 250
        self.max_health = 250
        self.attack = 0.6
        self.set_speed(1)
        self.set_loot_amount(5)