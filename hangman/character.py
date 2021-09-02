import pygame
import os

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super(Character, self).__init__()
        self.animations = [[] for x in range(5)]
        
        self.add_to_animation_matrix(0, 'idle1')
        self.add_to_animation_matrix(1, 'running')
        self.add_to_animation_matrix(2, 'jump')
        self.add_to_animation_matrix(3, 'attack1')
        self.add_to_animation_matrix(4, 'fall')
 
        self.row : int = 0
        self.column : int = 0
        self.right : bool = True
        self.x : int = 5
        self.y : int = 450
        self.lateral_speed : int = 6
        self.jumping : bool = False
        self.step : int = 0
 
        self.image = self.animations[self.row][self.column]
 
        self.rect = pygame.Rect(self.x, self.y, 90, 238)
    
    def add_to_animation_matrix(self, i, dir) -> None:
        for filename in os.listdir('character_sprite/Individual Sprites/' + dir + '/'):
                self.animations[i].append(pygame.image.load(os.path.join('character_sprite/Individual Sprites/' + dir + '/', filename)))

    def run_animation(self, dir : bool) -> None:
        self.right = dir
        if self.right:
            self.x += self.lateral_speed
        else:
            self.x -= self.lateral_speed
        self.rect = pygame.Rect(self.x, self.y, 90, 238)
        if not self.jumping:
            self.row = 1
        else:
            self.non_movement_animation(2)
    

    def attack_animation(self) -> None:
        self.row = 3

    def non_movement_animation(self, i : int) -> None:
        if self.jumping and self.step > 2:
            self.row = 4
        else:
            self.row = i
    
    def jump_animation(self) -> None:
        # Figure out if they are touching the ground
        
        if self.y  >= 450:
            self.row = 2
            self.jumping = True
    
    def calculate_height(self):
        if self.step < 8:
            self.y -= 10.2 * ((1/self.y) * 500)
            self.step += 1
        else:
            if self.step < 16:
                self.y += 10.2 * ((1/self.y) * 500)
                self.step += 1
            else:
                self.step = 0
                self.jumping = False
        self.rect = pygame.Rect(self.x, self.y, 90, 238)

 
    def update(self):
        if self.jumping:
            self.calculate_height()
            
        self.column += 1
 
        if self.column >= len(self.animations[self.row]):
            self.column = 0
        
        if  self.right:
            self.image = self.animations[self.row][self.column]
        else: 
            self.image = pygame.transform.flip(self.animations[self.row][self.column], True, False)
