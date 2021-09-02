import pygame
import os

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super(Character, self).__init__()
        #adding all the images to sprite array
        self.animations = [[], [], [], []]
        print(self.animations)
        
        self.add_to_animation_matrix(0, 'idle1')
        self.add_to_animation_matrix(1, 'running')
        self.add_to_animation_matrix(2, 'jump')
        self.add_to_animation_matrix(3, 'attack1')
 
        self.row = 0
        self.column = 0
        self.right = True
        self.x = 5
        self.y = 450
        self.lateral_speed = 6
        self.jumping = False
        self.step = 0
 
        self.image = self.animations[self.row][self.column]
 
        self.rect = pygame.Rect(self.x, self.y, 90, 238)
    
    def add_to_animation_matrix(self, i, dir):
        for filename in os.listdir('character_sprite/Individual Sprites/' + dir + '/'):
                self.animations[i].append(pygame.image.load(os.path.join('character_sprite/Individual Sprites/' + dir + '/', filename)))

    def run_animation(self, dir):
        self.right = dir
        if self.right:
            self.x += self.lateral_speed
        else:
            self.x -= self.lateral_speed
        self.rect = pygame.Rect(self.x, self.y, 90, 238)
        self.row = 1
    
    def non_movement_animation(self, i):
        self.row = i
    
    def jump_animation(self):
        # Figure out if they are touching the ground
        if self.y > 50:
            self.row = 2
            self.jumping = True
    
    def calculate_height(self):
        if self.step < 8:
            self.y -= 4.2 * (self.y * .01)
            self.step += 1
        else:
            if self.step < 16:
                self.y += 4.2 * (self.y * .01)
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
