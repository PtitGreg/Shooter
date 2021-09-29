import pygame

class SoundManager:
    
    def __init__(self):
        self.sounds = {
            "click": pygame.mixer.Sound("C:\\Users\\passi\\OneDrive\\Bibliothèque\\Programmation\\Projets python\\Jeu shooter\\assets\\sounds\\click.ogg"),
            "game_over": pygame.mixer.Sound("C:\\Users\\passi\\OneDrive\\Bibliothèque\\Programmation\\Projets python\\Jeu shooter\\assets\\sounds\\game_over.ogg"),
            "meteorite": pygame.mixer.Sound("C:\\Users\\passi\\OneDrive\\Bibliothèque\\Programmation\\Projets python\\Jeu shooter\\assets\\sounds\\meteorite.ogg"),
            "tir": pygame.mixer.Sound("C:\\Users\\passi\\OneDrive\\Bibliothèque\\Programmation\\Projets python\\Jeu shooter\\assets\\sounds\\tir.ogg"),
        }
        
    def play(self, name):
        self.sounds[name].play()