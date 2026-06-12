import pygame

class SoundManager:
    
    def __init__(self):
        self.sounds = {
            'click': pygame.mixer.Sound("html/python/assets/sounds/click.ogg"),
            'game_over': pygame.mixer.Sound("html/python/assets/sounds/game_over.ogg"),
            'meteorite': pygame.mixer.Sound("html/python/assets/sounds/meteorite.ogg"),
            'tir': pygame.mixer.Sound("html/python/assets/sounds/tir.ogg")
        }
        
    def play(self, name):
        self.sounds[name].play()