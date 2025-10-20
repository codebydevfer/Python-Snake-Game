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
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]

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
    # creating font obj my_font
    my_font = pygame.font.SysFont('times new roman', 50)

    # creating a text surface where text will be drawn
    game_over_surface = my_font.render('Your score is: ' + str(score), True, red)

    # creating a rectangular object for the text surface obj
    game_over_rect = game_over_surface.get_rect()

    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)

    # blit will drawn the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # after 2 seconds quit the program
    time.sleep(2)

    # deactivate pygame lib
    pygame.quit()

    # quit
    quit()

# main func
while True:
    # key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
    
    # If two keys pressed simultaneously, we don't want snake to move into two directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake body growing mechanism. If fruits and snakes collide then scores will be incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
        
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
        
    fruit_spawn = True
    game_window.fill(black)
    
    for pos in snake_body:
        pygame.draw.rect(game_window, green, 
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
      fruit_position[0], fruit_position[1], 10, 10))

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()#test
    
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    
    # displaying score continuously
    show_score(1, white, 'times new roman', 20)
    
    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)