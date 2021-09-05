import pygame
import os
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Enemy, self).__init__()
        self.animations = [[] for x in range(4)]
        self.directory : str = str(random.randrange(1,10))
        
        self.add_to_animation_matrix(0, 'idle')
        self.add_to_animation_matrix(1, 'walk')
        #self.add_to_animation_matrix(2, 'jump')
        self.add_to_animation_matrix(3, 'attack')


 
        self.row : int = 0
        self.column : int = 0
        self.right : bool = True
        self.x : int = x
        self.y : int = y
        self.lateral_speed : int = random.randrange(3,9)
        self.width : int = 90
        self.height : int = 73
        self.neg : int = 1
        self.health: int = 5
 
        self.image = self.animations[self.row][self.column]
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
 
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def add_to_animation_matrix(self, i, dir) -> None:
        for filename in os.listdir('enemy_sprite/' + self.directory + '/' + dir + '/'):
                self.animations[i].append(pygame.image.load(os.path.join('enemy_sprite/' + self.directory + '/' + dir + '/', filename)))


    def attack_player(self, player_x) -> None:
        if abs(player_x - self.x) > 300:
            self.row = 0
        else:
            if  abs(player_x - self.x) < 70:
                self.row = 3
            else: 
                self.row = 1
            if player_x < self.x:
                self.right = False
                self.x -= self.lateral_speed
            else:
                self.right = True
                self.x += self.lateral_speed
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
