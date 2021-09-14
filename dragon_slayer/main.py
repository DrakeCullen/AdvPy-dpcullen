#! /usr/bin/env python3

import pygame
import os
import sys
import pygame.freetype


characterPath = "./character.py"
sys.path.append(os.path.abspath(characterPath))
enemyPath = "./enemy.py"
sys.path.append(os.path.abspath(enemyPath))
dragonPath = "./dragon.py"
sys.path.append(os.path.abspath(dragonPath))
fireballPath = "./fireball.py"
sys.path.append(os.path.abspath(fireballPath))



import character
import enemy
import dragon
import fireball

WIDTH = 1000
HEIGHT = 650
BACKGROUND = pygame.image.load("background.png")
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
HEART = pygame.image.load("heart.png")
HEART = pygame.transform.scale(HEART, (60, 60))
pygame.init()
GAME_FONT = pygame.freetype.SysFont("Comic Sans MS", 36)

def pygame_setup(width : int, height: int) -> None:
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Game title goes here")  
    return screen


def menu(screen : pygame) -> None:
    showMenu : bool = True
    while showMenu:
        pygame.display.update()
        for event in pygame.event.get():
            showMenu = quit(event)
            if start_game(event):
                showMenu = game_loop(screen)
            

def game_loop(screen) -> None:
    playing : bool = True
    player : character.Character = character.Character()
    player_sprite : pygame.sprite = pygame.sprite.Group(player)
    clock : pygame.time = pygame.time.Clock()
    just_jumped : bool = False
    enemies, enemy_sprites = create_enemies(3, screen)
    dragons : dragon.Dragon = dragon.Dragon(150, 450, screen)
    dragon_sprite : pygame.sprite = pygame.sprite.Group(dragons)
    hurt_timer : int = 0
    counter = 0
    attacking = False
    score = 5000
    pygame.mixer.init()
    pygame.mixer.music.load('music.wav')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.2)
    
    while playing:
        pygame.display.update()
        for event in pygame.event.get():
            if not quit(event):
                return False

        key_input = pygame.key.get_pressed()  
        attacking, counter, just_jumped = determine_player_action(player, key_input, just_jumped, attacking, counter)
        x, dir = player.coordinates_and_dir()
        dragons.attack_player(x, dir)
       

        update_screen(enemies, enemy_sprites, player, player_sprite, dragons, dragon_sprite, screen)
        hurt_timer, playing = checkCollision(enemies, enemy_sprites, player, dragons, hurt_timer, screen)
        GAME_FONT.render_to(screen, (30, 20), f"Score: {score}", (255, 255, 255))
        pygame.display.update()
        clock.tick(30)
        hurt_timer += 1
        score -= 1


def quit(event) -> bool:
    return event.type != pygame.QUIT


def start_game(event) -> bool:
    if event.type == pygame.MOUSEBUTTONDOWN:
        return event.pos[0] in range(0, WIDTH) and event.pos[1] in range(0, HEIGHT)
    

def create_enemies(size : int, surface):
    enemies = []
    enemy_sprites = []
    for i in range(size):
        enemys : enemy.Enemy = enemy.Enemy(120 + i*150, 560, surface)
        enemy_sprite : pygame.sprite = pygame.sprite.Group(enemys)
        if i % 2:
            enemys.flip()
        enemies.append(enemys)
        enemy_sprites.append(enemy_sprite)
    return enemies, enemy_sprites

def update_screen(enemies, enemy_sprites, player, player_sprite, dragon, dragon_sprite, screen):
    screen.blit(BACKGROUND, [0,0])   
    draw_hearts(player) 
    for i in range(len(enemies)):
        enemies[i].attack_player(player.coordinates())
        enemy_sprites[i].update()
        enemy_sprites[i].draw(screen)
    player_sprite.update()
    player_sprite.draw(screen)
    dragon_sprite.update(screen)
    dragon_sprite.draw(screen)


def draw_hearts(player):
    for i in range(player.get_hearts()):
        screen.blit(HEART, [950 - i * 50,10]) 

def determine_player_action(player : character.Character, key_input : pygame.key, just_jumped, attacking, count):
    if  key_input[pygame.K_SPACE] and count < 8:
        attacking = True
    if attacking:
        if count < 12:
            player.attack_animation()
            count+=1
        else:
            attacking = False
        return attacking, count, True
    elif key_input[pygame.K_LEFT] or key_input[pygame.K_RIGHT] or key_input[pygame.K_UP] or key_input[pygame.K_DOWN]:
        if key_input[pygame.K_UP]:
            player.jump_animation(False)
        if key_input[pygame.K_LEFT]:
            player.run_animation(False)
        if key_input[pygame.K_RIGHT]:
            player.run_animation(True)
        if key_input[pygame.K_DOWN]:
            player.crouch_animation()
    else:
        player.non_movement_animation(0)
    if attacking == False:
        count += 1
    if count > 26:
        count = 0

    return attacking, count, False


def checkCollision(enemies, enemy_sprites, player, dragons, timer, screen):
    items_to_del = []
    for i in range(len(enemies) -1, -1, -1):
        x, y, width, height = enemies[i].coordinates()
        if player.enemy_collision(x, y, width, height, timer) != "None":
            if player.enemy_collision(x, y, width, height, timer) == "Hit":
                screen.fill((0,255,0), special_flags = pygame.BLEND_MULT)
                if enemies[i].hurt():
                    del enemies[i]  
                    del enemy_sprites[i]  
            elif timer > 40:
                screen.fill((255, min(255, max(0, round(255 * (1-.5)))), min(255, max(0, round(255 * (.5))))), special_flags = pygame.BLEND_MULT)
            timer = 0
    x, y, width, height = dragons.coordinates()
    if player.dragon_collision(x, y, width, height, timer) != "None":
        if player.dragon_collision(x, y, width, height, timer) == "Hit":
            screen.fill((0,255,0), special_flags = pygame.BLEND_MULT)
            if dragons.hurt():
                del dragons
                return timer, False
        elif timer > 40:    
            screen.fill((255, min(255, max(0, round(255 * (1-.5)))), min(255, max(0, round(255 * (.5))))), special_flags = pygame.BLEND_MULT)
        timer = 0
                    
    x, y = player.x_y_coordinates()
    hearts = player.get_hearts()
    rem_hearts = dragons.fire_collision(x,y, hearts)
    player.set_hearts(rem_hearts)
    if hearts != rem_hearts:
        screen.fill((255, min(255, max(0, round(255 * (1-.5)))), min(255, max(0, round(255 * (.5))))), special_flags = pygame.BLEND_MULT)
    return timer, True
    
    

 
if __name__ == '__main__':
    screen = pygame_setup(WIDTH, HEIGHT)

    menu(screen)