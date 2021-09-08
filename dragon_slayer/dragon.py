import pygame
import os
import random
import sys
import datetime

fireballPath = "./fireball.py"
sys.path.append(os.path.abspath(fireballPath))
import fireball

class Dragon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Dragon, self).__init__()
        self.animations = [[] for x in range(7)]
        
        self.add_to_animation_matrix(0, 'idle')
        self.add_to_animation_matrix(1, 'walk')
        self.add_to_animation_matrix(2, 'attack1')


 
        self.row : int = 0
        self.column : int = 0
        self.right : bool = True
        self.x : int = x
        self.y : int = y
        self.lateral_speed : int = 11
        self.width : int = 280
        self.height : int =  250
        self.neg : int = 1
        self.health: int = 14
        self.counter = 0
        self.last_hurt_time = datetime.datetime.now()
        
        self.fireballs = []
        self.fireball_sprites = []
        
        self.image = self.animations[self.row][self.column]
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
 
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def add_to_animation_matrix(self, i, dir) -> None:
        for filename in os.listdir('dragon/' + dir + '/'):
                self.animations[i].append(pygame.image.load(os.path.join('dragon/' + dir + '/', filename)))


    def attack_player(self, player_x, player_right) -> None:
        self.add_fireball()
        self.wall_collision()
        self.row = 1
        self.counter += 1
        if not self.wall_collision():
            if self.counter > 15:
                if random.randrange(2) == 1: 
                    self.neg *= -1
                    self.right = not self.right
                self.counter = 0
            self.x += self.lateral_speed * self.neg
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        
    def add_fireball(self):
        if random.randrange(30) == 1:
            if self.right:
                new_fireball : fireball.Fireball = fireball.Fireball(self.x + self.width - 95, 530, self.right)
            else:
                new_fireball : fireball.Fireball = fireball.Fireball(self.x, 530, self.right)
            self.fireballs.append(new_fireball)
            fireball_sprite : pygame.sprite = pygame.sprite.Group(new_fireball)
            self.fireball_sprites.append(fireball_sprite)
            
    def coordinates(self) :
        if not self.right:
            return self.x + 100, self.y, 90, self.height
        return self.x + 100, self.y, 100, self.height
    
    def flip(self):
        self.right = False
        
    def hurt(self):
        self.health -= 1
        if self.health <= 0:
            return True
        return False

    def wall_collision(self) -> bool:
        if  self.x + self.width <= self.width:
            self.right = not self.right
            self.neg *= -1
            self.x += self.lateral_speed * self.neg
            self.counter = 0
            return True
        elif self.x + self.width >= 1000:
            self.right = not self.right
            self.neg *= -1
            self.x += self.lateral_speed * self.neg
            self.counter = 0
            return True
        return False
    
    
    def fire_collision(self, player_x, player_y, hearts):
        for i in range(len(self.fireballs)):
            enemy_x, enemy_y, enemy_width, enemy_height = self.fireballs[i].coordinates()
            if  (datetime.datetime.now() - self.last_hurt_time).total_seconds() > 2 and player_x <= enemy_x + enemy_width and player_x + 67 >= enemy_x and player_y + 40 >= enemy_y:
                self.last_hurt_time = datetime.datetime.now()
                hearts -= 1
                print(hearts)
        return hearts
    
    
    def update(self, screen):
        for i in range(len(self.fireballs)):
            self.fireballs[i].move()
            self.fireball_sprites[i].update()
            self.fireball_sprites[i].draw(screen)

        self.column += 1
 
        if self.column >= len(self.animations[self.row]):
            self.column = 0
        
        if  self.right:
            self.image = self.animations[self.row][self.column]
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
        else: 
            self.image = pygame.transform.flip(self.animations[self.row][self.column], True, False)
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
