import pygame
import time
import random

snake_speed = 15


# window size 
window_x = 720
window_y = 480

#colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color (0, 0, 255)

#initialize pygame
pygame.init()

#initialize game window
pygame.display.set_caption("Snake Game")
game_window = pygame.display.set_mode((window_x, window_y))

#fps controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

# first 4 blocks of snake body
snake_body = [ [100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

# fruit position
fruit_position = [random.randrange(1, (window_x//10) * 10),
                  random.randrange(1, (window_y//10) * 10)]

fruit_spawn = True

# default snake direction towards right
direction = 'RIGHT'
change_to = direction

#player score
#initial score
score = 0

# display score func
def show_score(choice, color, font, size):
    # font obj score_font
    score_font = pygame.font.SysFont(font, size)

    # display surface obj score surface
    score_surface = score_font.render('Score: ' + str(score), True, color)

    #rectangular obj for the text surface obj 
    score_rect = score_surface.get_rect()

    # display text
    game_window.blit(score_surface, score_rect)

# game over func
def game_over():
    