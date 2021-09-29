from projectile import Projectile
import pygame
import animation


# creer une premiere class pour representer le joueur
class Player(animation.AnimateSprite): 

    def __init__(self, game): 
        super().__init__("player")
        self.game = game
        self.health          = 100
        self.max_health      = 100
        self.attack          = 10
        self.velocity        = 8
        self.all_projectiles = pygame.sprite.Group()
        self.rect            = self.image.get_rect()
        self.rect.x          = 400
        self.rect.y          = 710
        
        
    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            #si le joueur n'a plus de points de vie
            self.game.game_over()
            
    def update_animation(self):
        self.animate()
        
    def update_health_bar(self, surface):
        #dessiner notre bar de vie
        pygame.draw.rect(surface, (51, 64, 55), [self.rect.x + 50, self.rect.y + 0, self.max_health, 10])
        pygame.draw.rect(surface, (30, 184, 81), [self.rect.x + 50, self.rect.y + 0, self.health, 10])
        
        
        
    def launch_projectile(self):
        #creer nouvelle instance classe projectile
        self.all_projectiles.add(Projectile(self))
        #demarrer l'animation
        self.start_animation()
        #jouer le son
        self.game.sound_manager.play("tir")
        
    def move_right(self): 
        #si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity
        #si le monstre est en collision avec le joueur
        else:
            #infliger des degats
            self.game.player.damage(self.attack)
            
    def move_left(self) : 
        self.rect.x -= self.velocity