#! /usr/bin/env python3

import pygame
import os
import sys

characterPath = "./character.py"
sys.path.append(os.path.abspath(characterPath))
BACKGROUND_COLOR = pygame.Color('white') 

import character

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

    while playing:
        pygame.display.update()
        for event in pygame.event.get():
            if not quit(event):
                return False

        key_input = pygame.key.get_pressed()  
        determine_player_action(player, key_input)
       
        player_sprite.update()
        screen.fill(BACKGROUND_COLOR)
        player_sprite.draw(screen)
        pygame.display.update()
        clock.tick(15)

def quit(event) -> bool:
    return event.type != pygame.QUIT


def start_game(event) -> bool:
    if event.type == pygame.MOUSEBUTTONDOWN:
        return event.pos[0] in range(0, 800) and event.pos[1] in range(0, 500)

def determine_player_action(player : character.Character, key_input : pygame.key):
    if key_input[pygame.K_LEFT] or key_input[pygame.K_RIGHT] or key_input[pygame.K_UP] or key_input[pygame.K_SPACE]:
        if key_input[pygame.K_LEFT]:
            player.run_animation(False)
        if key_input[pygame.K_RIGHT]:
            player.run_animation(True)
        if key_input[pygame.K_UP]:
            player.jump_animation()
        if key_input[pygame.K_SPACE]:
            player.attack_animation()
    else:
        player.non_movement_animation(0)

 
if __name__ == '__main__':
    screen = pygame_setup(800, 500)

    menu(screen)