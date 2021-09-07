import pygame
import os
import random

class Dragon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Dragon, self).__init__()
        self.animations = [[] for x in range(7)]
        
        self.add_to_animation_matrix(0, 'idle')
        self.add_to_animation_matrix(1, 'walk')
        self.add_to_animation_matrix(2, 'attack1')
        self.add_to_animation_matrix(3, 'attack2')
        self.add_to_animation_matrix(4, 'attack3')
        self.add_to_animation_matrix(5, 'attack4')
        self.add_to_animation_matrix(6, 'attack5')


 
        self.row : int = 0
        self.column : int = 0
        self.right : bool = True
        self.x : int = x
        self.y : int = y
        self.lateral_speed : int = 14
        self.width : int = 280
        self.height : int =  250
        self.neg : int = 1
        self.health: int = 14
        self.counter = 0
 
        self.image = self.animations[self.row][self.column]
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
 
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def add_to_animation_matrix(self, i, dir) -> None:
        for filename in os.listdir('dragon/' + dir + '/'):
                self.animations[i].append(pygame.image.load(os.path.join('dragon/' + dir + '/', filename)))


    def attack_player(self, player_x, player_right) -> None:
        if not self.right and  abs(player_x - self.x) < 20 :
            self.row = 2
            if (self.right and player_right) or (self.right and not player_right):
                self.right = not self.right  
        else: 
            self.row = 1
            self.counter += 1
            if self.counter > 20:
                if random.randrange(2) == 1: 
                    self.neg *= -1
                    self.right = not self.right
                self.counter = 0
            self.x += self.lateral_speed * self.neg
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def coordinates(self) :
        if not self.right:
            return self.x + 30, self.y, 25, self.height
        return self.x, self.y, 20, self.height
    
    def flip(self):
        self.right = False
        
    def hurt(self):
        self.health -= 1
        if self.health > 0:
            if self.right:
                self.x -= 45 
            else:
                self.x += 45
        else:
            return True
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return False
    
    def update(self):
        self.column += 1
 
        if self.column >= len(self.animations[self.row]):
            self.column = 0
        
        if  self.right:
            self.image = self.animations[self.row][self.column]
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
        else: 
            self.image = pygame.transform.flip(self.animations[self.row][self.column], True, False)
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
