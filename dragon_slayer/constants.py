import pygame
import pygame.freetype

WIDTH = 1000
HEIGHT = 650
BACKGROUND = pygame.image.load("graphics/background.png")
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
HOME = pygame.image.load("graphics/home-screen.png")
HOME = pygame.transform.scale(HOME, (WIDTH, HEIGHT))
INSTRUCTIONS = pygame.image.load("graphics/instructions.png")
INSTRUCTIONS = pygame.transform.scale(INSTRUCTIONS, (WIDTH, HEIGHT))
HEART = pygame.image.load("graphics/heart.png")
HEART = pygame.transform.scale(HEART, (60, 60))
GOLDHEART = pygame.image.load("graphics/gold-heart.png")
GOLDHEART = pygame.transform.scale(GOLDHEART, (60, 60))
NOATTACK = pygame.image.load("graphics/no-attack.png")
NOATTACK = pygame.transform.scale(NOATTACK, (60, 50))
GAME_FONT = pygame.freetype.SysFont("Comic Sans MS", 36)
