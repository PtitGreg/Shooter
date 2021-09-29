import pygame

# definir class gestion projectile
class Projectile(pygame.sprite.Sprite): 
    
    #definir le constructeur de cette class
    def __init__(self, player): 
        super().__init__()
        self.velocity     = 5
        self.player       = player
        self.image        = pygame.image.load("C:\\Users\\passi\\OneDrive\\Bibliothèque\\Programmation\\Projets python\\Jeu shooter\\assets\\projectile.png")
        self.image        = pygame.transform.scale(self.image, (50,50))
        self.rect         = self.image.get_rect()
        self.rect.x       = player.rect.x  + 130
        self.rect.y       = player.rect.y + 100
        self.origin_image = self.image
        self.angle = 0
        
    def rotate(self):
        #tourner le projectile
        self.angle += 1
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
        
    def remove(self):
        self.player.all_projectiles.remove(self)
        
    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        
        #verifier si le projectile entre en collision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            #infliger des degats
            monster.damage(self.player.attack)
        
        #verif du projectile hors ecran
        if self.rect.x > 1920:
            #supprimer le projectile ( en dehors de l'ecran)
            self.remove()