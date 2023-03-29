import pygame, random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

def restart_game_question():
    font = pygame.font.Font('freesansbold.ttf', 18)
    question = font.render('Do you want play again Y/N?', True, (255,255,255))
    rect = question.get_rect()
    rect.topleft = (20, 500)
    screen.blit(question, rect)

    while True:
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_y:
                    main_game()
                if event.key == K_n:
                    pygame.quit()
                    exit()

        pygame.display.update()

def main_game():
    snake = [(200, 200),(210, 200), (220, 200)]
    snake_skin = pygame.Surface((10,10))
    snake_skin.fill((255,255,255))

    food_pos = on_grid_random()
    food = pygame.Surface((10,10))
    food.fill((255,0,0))

    my_direction = LEFT

    clock = pygame.time.Clock()

    font = pygame.font.Font('freesansbold.ttf', 18)
    score = 0

    game_over = False

    while not game_over:
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
                
            if event.type == KEYDOWN:
                if event.key == K_UP and my_direction != DOWN:
                    my_direction = UP
                if event.key == K_DOWN and my_direction != UP:
                    my_direction = DOWN
                if event.key == K_LEFT and my_direction != RIGHT:
                    my_direction = LEFT
                if event.key == K_RIGHT and my_direction != LEFT:
                    my_direction = RIGHT
                    
                
        if collision(snake[0], food_pos):
            food_pos = on_grid_random()
            snake.append((0,0))
            score = score + 1

        
            
        # Check if the snake has collided with boundaries
        if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake [0][1] < 0:
            game_over = True
            break
        
        # Check if the snake has collided with itself
        for i in range(1, len(snake) - 1):
            if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
                game_over = True
                break
            
        if game_over:
            break

        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i-1][0], snake[i-1][1])


        #Snake movements 
        if my_direction ==  UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
        if my_direction ==  DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
        if my_direction ==  RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])
        if my_direction ==  LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])            
                
        screen.fill((0,0,0))
        screen.blit(food, food_pos)
        
        score_font = font.render('Score: %s' % (score), True, (255,255,255))
        score_rect = score_font.get_rect()
        score_rect.topleft = (20, 10)
        screen.blit(score_font, score_rect)

        for pos in snake: 
            screen.blit(snake_skin, pos)
                
        pygame.display.update()

    while True:
        game_over_font = pygame.font.Font('freesansbold.ttf', 75)
        game_over_screen = game_over_font.render('Game Over', True, (255,255,255))
        game_over_rect = game_over_screen.get_rect()
        game_over_rect.midtop = (600 / 2, 100)
        screen.blit(game_over_screen, game_over_rect)
        restart_game_question()
        pygame.display.update()
        pygame.time.wait(500)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

main_game()            