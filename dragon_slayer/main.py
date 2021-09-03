#! /usr/bin/env python3

import pygame
import os
import sys

characterPath = "./character.py"
sys.path.append(os.path.abspath(characterPath))
enemyPath = "./enemy.py"
sys.path.append(os.path.abspath(enemyPath))

import character
import enemy

WIDTH = 1000
HEIGHT = 650
BACKGROUND = pygame.image.load("background.png")
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

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
    enemys : enemy.Enemy = enemy.Enemy()
    enemy_sprite : pygame.sprite = pygame.sprite.Group(enemys)
    clock : pygame.time = pygame.time.Clock()
    just_jumped : bool = False

    while playing:
        pygame.display.update()
        for event in pygame.event.get():
            if not quit(event):
                return False

        key_input = pygame.key.get_pressed()  
        just_jumped = determine_player_action(player, key_input, just_jumped)
       
        enemys.non_movement_animation(1)
        player_sprite.update()
        enemy_sprite.update()
        screen.blit(BACKGROUND, [0,0])        
        player_sprite.draw(screen)
        enemy_sprite.draw(screen)
        pygame.display.update()
        clock.tick(13)

def quit(event) -> bool:
    return event.type != pygame.QUIT


def start_game(event) -> bool:
    if event.type == pygame.MOUSEBUTTONDOWN:
        return event.pos[0] in range(0, WIDTH) and event.pos[1] in range(0, HEIGHT)

def determine_player_action(player : character.Character, key_input : pygame.key, just_jumped):
    if key_input[pygame.K_LEFT] or key_input[pygame.K_RIGHT] or key_input[pygame.K_UP] or key_input[pygame.K_SPACE] or key_input[pygame.K_DOWN]:
        if key_input[pygame.K_LEFT]:
            player.run_animation(False)
        if key_input[pygame.K_RIGHT]:
            player.run_animation(True)
        if key_input[pygame.K_UP]:
            player.jump_animation(just_jumped)
            return True
        if key_input[pygame.K_SPACE]:
            player.attack_animation()
        if key_input[pygame.K_DOWN]:
            player.crouch_animation()
    else:
        player.non_movement_animation(0)
    return False

 
if __name__ == '__main__':
    screen = pygame_setup(WIDTH, HEIGHT)

    menu(screen)