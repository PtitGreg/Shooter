import pygame
import math
from game import Game
pygame.init()

#definir une clock
clock = pygame.time.Clock()
FPS = 60

# generer la fenetre du jeu
pygame.display.set_caption("Jeu Shooter")
screen = pygame.display.set_mode((1920, 1080))

# importer pour charger l'arriere plan du jeu
background = pygame.image.load("C:\\Users\\passi\\OneDrive\\Bibliothèque\\Programmation\\Projets python\\Jeu shooter\\assets\\bg.jpg")

#importer charger notre banniere
banner = pygame.image.load("C:\\Users\\passi\\OneDrive\\Bibliothèque\\Programmation\\Projets python\\Jeu shooter\\assets\\banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 3)

#importer charger notre bouton pour lancer la partie
play_button = pygame.image.load("C:\\Users\\passi\\OneDrive\\Bibliothèque\\Programmation\\Projets python\\Jeu shooter\\assets\\button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.75)
play_button_rect.y = math.ceil(screen.get_height() / 2.8)

#charger le jeu
game = Game()

running = True

# boucle tant que cette condition est vrai
while running:
    #appliquer l'arriere plan du jeu
    screen.blit(background, (0, 5))
        
    #verifier si le jeu a commencé ou non
    if game.is_playing:
        #declencher les instructiuons de la partie
        game.update(screen)
    #verifier si notre jeu n'a pas commencé  
    else:
        #ajouter ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

        
    # mise a jour ecran
    pygame.display.flip()
    
    # si joueur ferme la fenetre
    for event in pygame.event.get(): 
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT: 
            running = False
            pygame.quit()
            print("Fermeture du jeu")         
        #detecter si le joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN: 
            game.pressed[event.key] = True
            
            #detecter si touche espace est enclenchee pour lancer notre projectile
            if event.key == pygame.K_SPACE: 
                if game.is_playing:
                   game.player.launch_projectile()
                else:
                    #mettre le jeu en mode lancé
                    game.start()
                    #jouer le son
                    game.sound_manager.play("click")
            
        elif event.type == pygame.KEYUP: 
            game.pressed[event.key] = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verifier pour savoir si la souris est en collision avec le bouton
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode lancé
                game.start()
                #jouer le son
                game.sound_manager.play("click")
    #fixer nombre de fps sur ma clock
    clock.tick(FPS)