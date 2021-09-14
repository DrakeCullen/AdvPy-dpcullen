import pygame
import os
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, surface):
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
        self.lateral_speed : int = random.randrange(2,6)
        self.width : int = 90
        self.height : int = 73
        self.neg : int = 1
        self.health: int = random.randrange(7,15)
 
        self.image = self.animations[self.row][self.column]
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.surface = surface
 
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def add_to_animation_matrix(self, i, dir) -> None:
        for filename in os.listdir('enemy_sprite/' + self.directory + '/' + dir + '/'):
                self.animations[i].append(pygame.image.load(os.path.join('enemy_sprite/' + self.directory + '/' + dir + '/', filename)))


    def attack_player(self, player_x) -> None:
        if abs(player_x - self.x) > 600:
            self.row = 0
        else:
            if  abs(player_x - self.x) < 80:
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
                self.x -= 65 
            else:
                self.x += 65
        else:
            return True
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return False

    def draw_health_bar(self):
        if self.health > 3:
            if not self.right:
                pygame.draw.rect(self.surface, (0,255,0), pygame.Rect(self.x + self.width / 2.5, self.y, 5 * self.health, 10))
            else:
                pygame.draw.rect(self.surface, (0,255,0), pygame.Rect(self.x + 6, self.y, 5 * self.health, 10))
        else:
            if not self.right:
                pygame.draw.rect(self.surface, (255,0,0), pygame.Rect(self.x + self.width / 2.5, self.y, 5 * self.health, 10))
            else:
                pygame.draw.rect(self.surface, (255,0,0), pygame.Rect(self.x + 10, self.y, 5 * self.health, 10))
    
    def update(self):
        self.draw_health_bar()
        self.column += 1
 
        if self.column >= len(self.animations[self.row]):
            self.column = 0
        
        if  self.right:
            self.image = self.animations[self.row][self.column]
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
        else: 
            self.image = pygame.transform.flip(self.animations[self.row][self.column], True, False)
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
