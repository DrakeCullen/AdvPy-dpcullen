import pygame
import os
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.animations = [[] for x in range(4)]
        
        self.add_to_animation_matrix(0, 'idle')
        self.add_to_animation_matrix(1, 'walk')
        self.add_to_animation_matrix(2, 'jump')
        self.add_to_animation_matrix(3, 'attack')
        #self.add_to_animation_matrix(4, 'fall')
        #self.add_to_animation_matrix(5, 'crouch')
 
        self.row : int = 0
        self.column : int = 0
        self.right : bool = True
        self.x : int = 150
        self.y : int = 560
        self.lateral_speed : int = 7
        self.jumping : bool = False
        self.step : int = 0
        self.ground : int = 560
        self.player_width : int = 90
        self.player_height : int = 73
        self.counter = 0
        self.neg = 1
 
        self.image = self.animations[self.row][self.column]
        self.image = pygame.transform.scale(self.image, (self.player_width, self.player_height))
 
        self.rect = pygame.Rect(self.x, self.y, self.player_width, self.player_width)
    
    def add_to_animation_matrix(self, i, dir) -> None:
        for filename in os.listdir('enemy_sprite/' + dir + '/'):
                self.animations[i].append(pygame.image.load(os.path.join('enemy_sprite/' + dir + '/', filename)))


    def non_movement_animation(self, i : int) -> None:
        self.row = i
        self.counter += 1
        if self.counter > 20:
            if random.randrange(2) == 1: 
                self.neg *= -1
                self.right = not self.right
            self.counter = 0
        self.x += self.lateral_speed * self.neg
        self.rect = pygame.Rect(self.x, self.y, self.player_width, self.player_width)

    
    def update(self):
        self.column += 1
 
        if self.column >= len(self.animations[self.row]):
            self.column = 0
        
        if  self.right:
            self.image = self.animations[self.row][self.column]
            self.image = pygame.transform.scale(self.image, (self.player_width, self.player_height))
        else: 
            self.image = pygame.transform.flip(self.animations[self.row][self.column], True, False)
            self.image = pygame.transform.scale(self.image, (self.player_width, self.player_height))
