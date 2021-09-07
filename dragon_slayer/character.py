import pygame
import os

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super(Character, self).__init__()
        self.animations = [[] for x in range(6)]
        
        self.add_to_animation_matrix(0, 'idle1')
        self.add_to_animation_matrix(1, 'running')
        self.add_to_animation_matrix(2, 'jump2')
        self.add_to_animation_matrix(3, 'attack1')
        self.add_to_animation_matrix(4, 'fall')
        self.add_to_animation_matrix(5, 'crouch')
 
        self.row : int = 0
        self.column : int = 0
        self.right : bool = True
        self.x : int = 600
        self.y : int = 560
        self.lateral_speed : int = 16
        self.jumping : bool = False
        self.step : int = 0
        self.ground : int = 560
        self.player_width : int = 35
        self.width_right : int = 67
        self.player_height : int = 0
        self.hearts : int = 5
 
        self.image = self.animations[self.row][self.column]
 
        self.rect = pygame.Rect(self.x, self.y, self.player_width, self.player_height)
    
    def add_to_animation_matrix(self, i, dir) -> None:
        for filename in os.listdir('character_sprite/Individual Sprites/' + dir + '/'):
                self.animations[i].append(pygame.image.load(os.path.join('character_sprite/Individual Sprites/' + dir + '/', filename)))

    def run_animation(self, dir : bool) -> None:
        self.right = dir
        if self.right:
            if not self.wall_collision_right():
                self.x += self.lateral_speed
        else:
            if not self.wall_collision_left():
                self.x -= self.lateral_speed
        self.rect = pygame.Rect(self.x, self.y, self.player_width, self.player_height)
        if not self.jumping:
            self.row = 1
        else:
            self.non_movement_animation(2)
    

    def attack_animation(self) -> None:
        self.row = 3

    def non_movement_animation(self, i : int) -> None:
        self.player_height = 0
        if self.jumping and self.step > 1:
            self.row = 4
        else:
            self.row = i
    
    def jump_animation(self, held : bool) -> None:
        if self.y  >= 560 and not held:
            self.row = 2
            self.jumping = True
        else:
            self.row = 4
        
                
    def crouch_animation(self) -> None:
        if not self.jumping:
            self.row = 5
            self.player_height = 20
    
    def calculate_height(self):
        if self.step < 8:
            self.y -= 18.2 * ((1/self.y) * 500)
            self.step += 1
        else:
            if self.y + 20 < self.ground:
                self.y += 13.2 * ((1/self.y) * 500)
                self.step += 1
            else:
                self.y = self.ground
                self.step = 0
                self.jumping = False
        self.rect = pygame.Rect(self.x, self.y, self.player_width, self.player_height)

    def wall_collision_left(self) -> bool:
        if  self.x + self.player_width <= 0:
            return True
        return False
    
    def wall_collision_right(self) -> bool:
        if self.x + self.width_right >= 1000:
            return True
        return False
    
    def enemy_collision(self, enemy_x, enemy_y, enemy_width, enemy_height) -> str:
        player_x = self.x

        if  player_x <= enemy_x + enemy_width and player_x + self.width_right >= enemy_x and self.y + self.player_height >= enemy_y:#not self.y + self.player_height - enemy_height >= enemy_y and not self.y <= enemy_y - enemy_height :
                if self.row == 3:
                    print("hit")
                    return "Hit"
                else:
                    self.hearts -= 1
                    print(self.hearts)
                    return "Hurt"
        return "None"

    def coordinates(self) :
        return self.x

    def coordinates_and_dir(self):
        return self.x, self.right
    
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
