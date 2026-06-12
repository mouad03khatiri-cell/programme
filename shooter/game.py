from sounds import SoundManager
from player import Player
from monster import Alien, Monster, Mummy
from comet_event import CometFallEvent
import pygame

# cree une sconde classe qui va representer notre jeu
class Game:
    
    def __init__(self):
        # definir si notre jeu a commence ou non
        self.is_playing = False
        # generer le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # generer l'evenement
        self.comet_event = CometFallEvent(self)
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        # gerer le son
        self.sound_manager = SoundManager()
        # fonction pour press space to start
        self.touch = f"press s to start"
        # mettre le score a 0
        self.score = 0
        self.font = pygame.font.Font("html/python/assets/fonts/OakSans-Regular.ttf", 25)
        self.pressed = {}
        
    def start(self):
        self.player.rect.x = 200
        self.player.rect.y = 500
        self.is_playing = True
        self.comet_event.reset_percent()
        self.comet_event.fall_mode = False
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)
        
    def add_score(self, points=1):
        self.score += points
        
    def game_over(self):
        # remettre le jeu a neuf
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.comet_event.reset_percent()
        self.score = 0
        # joueur le son
        self.sound_manager.play('game_over')
        
    def update(self, screen):
        # afficher le score sur l'ecran
        score_text = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))
        
        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)
        
        # actualiser la barre du vie du joueur
        self.player.update_health_bar(screen)
        
        # actualiser la barre d'evenement
        self.comet_event.update_bar(screen)
        
        # actualiser l'animation du joueur
        self.player.update_animation()
        
        # recuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()
        
        # appliquer l'ensemble des images de mon groupes de projectile
        self.player.all_projectiles.draw(screen)
        
        # appliquer l'ensemble des images de mon groupe de monstre
        self.all_monsters.draw(screen)
        
        # apliquer des images de mon groupe de comettes
        self.comet_event.all_comets.draw(screen)
        
        # recuperer les monstre de notre jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()
            
        # recuperer les cometes de notre jeu
        for comet in self.comet_event.all_comets:
            comet.fall()

        # verifier si le joueur souhaite aller a droite ou a gauche
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
        
    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))