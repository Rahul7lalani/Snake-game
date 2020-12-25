import pygame
import time
import random

# pygame window
pygame.init()
clock = pygame.time.Clock()
# Colors using RGB
blackcolor = (0,0,0)
orangecolor = (255,123,7)
redcolor = (213,50,80)
greencolor = (0,255,0)
bluecolor=(50,153,213)

# Display window
width = 620
height = 410
displayz = pygame.display.set_mode((width,height))
# Caption
pygame.display.set_caption('Fun Snake Game')
snake_block = 12
snake_speed = 15
snake_list = []

# defining snake position and look
def snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(displayz,greencolor,[x[0],x[1],snake_block,snake_block])
# main cell
def snakegame():
    game_over = False
    game_end =False
    # x and y coordinates
    x1 = width/2
    y1 = height/2

    # changing coordinates according to
    x1_change = 0
    y1_change = 0

    # defining length of snake
    snake_list = []
    length_of_snake = 1

    # the coordinates of food
    foodx= round(random.randrange(0,width-snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0,height-snake_block) / 10.0) * 10.0
    while not game_over:
        while game_end == True:
            displayz.fill(bluecolor)
            font_style = pygame.font.SysFont("comicsansms",27)
            msg = font_style.render("Game Over!Wanna play again? Press R",True,orangecolor)
            displayz.blit(msg,[width/6,height/3])

            # displaying score
            score = length_of_snake -1
            score_font = pygame.font.SysFont("comicsansms",37)
            value = score_font.render("Your Score:"+ str(score),True,redcolor)
            displayz.blit(value,[width/3,height/5])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        snakegame()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_end = False         # game has been ended

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_end = True
        pygame.display.update()

        # updatation
        x1 += x1_change
        y1 += y1_change
        displayz.fill(blackcolor)
        pygame.draw.rect(displayz,redcolor,[foodx,foody,snake_block,snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)

        # when the length of the snake exceeds ,delete the snake_list
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        pygame.display.update()

        # when snake hits itself ,game ends
        for x in snake_list[:-1]:
            if x == snake_Head:
                game_end = True
        snake(snake_block,snake_list)
        pygame.display.update()

        # when snake hits the food ,the length of the snake is incremented by 1
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
        clock.tick(snake_speed)
        pygame.display.update()
    pygame.quit()
    quit()
snakegame()

