import pygame
import os
import sys

scriptpath = "./character.py"

sys.path.append(os.path.abspath(scriptpath))
BACKGROUND_COLOR = pygame.Color('white') 


import character

def pygame_setup(width : int, height: int) -> None:
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Game title goes here")
    return screen


def menu(screen) -> None:
    showMenu : bool = True
    while showMenu:
        pygame.display.update()
        for event in pygame.event.get():
            showMenu = quit(event)
            if start_game(event):
                game_loop(screen)
            


def game_loop(screen) -> None:
    playing : bool = True
    player = character.Character()
    player_sprite = pygame.sprite.Group(player)
 
    clock = pygame.time.Clock()
    while playing:
        pygame.display.update()
        for event in pygame.event.get():
            playing = quit(event)

        key_input = pygame.key.get_pressed()  
        if key_input[pygame.K_LEFT] or key_input[pygame.K_RIGHT] or key_input[pygame.K_UP] or key_input[pygame.K_SPACE]:
            if key_input[pygame.K_LEFT]:
                player.run_animation(False)
            if key_input[pygame.K_RIGHT]:
                player.run_animation(True)
            if key_input[pygame.K_UP]:
                player.jump_animation()
            if key_input[pygame.K_SPACE]:
                player.non_movement_animation(3)
        else:
            player.non_movement_animation(0)
        player_sprite.update()
 
        #filling the screen with background color
        screen.fill(BACKGROUND_COLOR)
 
        #drawing the sprite
        player_sprite.draw(screen)
 
        #updating the display
        pygame.display.update()
 
        #finally delaying the loop to with clock tick for 10fps 
        clock.tick(10)


def quit(event) -> bool:
    if event.type == pygame.QUIT:
        return False
    return True



def start_game(event) -> bool:
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.pos[0] in range(0, 800) and event.pos[1] in range(0, 500):
            return True
    return False
                                    


 
if __name__ == '__main__':
    screen = pygame_setup(800, 500)

    menu(screen)