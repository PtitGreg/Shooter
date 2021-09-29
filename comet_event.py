import pygame
from comet import Comet

#creer classe pour gerer cet event
class CometFallEvent:
    
    #lors du chargement -> creer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 20
        self.game = game
        self.fall_mode = False
        
        # definir un groupe de sprite pour stocker nos cometes
        self.all_comets = pygame.sprite.Group()
        
    def add_percent(self):
        self.percent += self.percent_speed / 100
        
    def is_full_loaded(self):
        return self.percent >= 100
    
    def reset_percent(self):
            self.percent = 0
    
    def meteor_fall(self):
        # boucle pour les valeurs entre 1 et 10
        for i in range(3, 30):
            #apparition 1ere boule de feu
            self.all_comets.add(Comet(self))
    
    def attempt_fall(self):
        #la jauge d'event est a 100%
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("Pluie de comètes !!!")
            self.meteor_fall()
            self.fall_mode = True # activer evenement
        
    def update_bar(self, surface):
        
        #ajouter du pourcentage a la bar
        self.add_percent()     
        
        #barre noir (en arriere pln)
        pygame.draw.rect(surface, (0, 0, 0), [
            0, #l'axe des x
            surface.get_height() - 55, #l'axe des y
            surface.get_width(), #longueur de fenetre
            10 #epaisseur de la barre
        ])
        #barre rouge (jauge d'event)
        pygame.draw.rect(surface, (187, 11, 11), [
            0, #l'axe des x
            surface.get_height() - 55, #l'axe des y
            (surface.get_width() / 100) * self.percent, #longueur de fenetre
            10 #epaisseur de la barre
        ])