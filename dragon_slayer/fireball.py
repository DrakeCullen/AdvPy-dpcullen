import pygame
import os
import random

class Fireball(pygame.sprite.Sprite):
    def __init__(self, x, y, right):
        super(Fireball, self).__init__()
        self.x : int = x
        self.y : int = y
        self.right : bool = right
        self.lateral_speed : int = 8
        self.width : int = 40
        self.height : int =  30
    
 
        self.image = pygame.image.load("./dragon/fireball/Fire_Attack4.png")
        if not self.right:
            self.image = pygame.transform.flip(self.image, True, False)
 
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self) -> None:
        if self.right:
            self.x += self.lateral_speed
        else:
            self.x -= self.lateral_speed
        
    def coordinates(self) :
         if not self.right:
                return self.x + 15, self.y, 30, self.height
         return self.x, self.y, 30, self.height
    
    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
