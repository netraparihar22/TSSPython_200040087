import pygame as pg
import random

pg.init()

#colors used
white = (255,255,255)
black = (0,0,0)
red= (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#game window
screen_width= 720
screen_height= 480
gameWindow = pg.display.set_mode((screen_width, screen_height))

#bg img
bg_img = pg.image.load("bgimg.jpg")
bg_img = pg.transform.scale(bg_img, (screen_width, screen_height)).convert_alpha()

#game title
pg.display.set_caption('Snake Eater')
pg.display.update()


clock = pg.time.Clock()
font = pg.font.SysFont(None, 25)

def text_screen(text, color, x, y):
    screen_text = font.render(text , True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pg.draw.rect(gameWindow, color, [x, y , snake_size, snake_size])   


#main loop
def GameLoop() :

    #game related variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    vel_x = 0
    vel_y = 0
    
    snake_list=[]
    snake_length = 1

    #food
    food_x = random.randint(10, screen_width/1.5)
    food_y = random.randint(10, screen_height/1.5)

    score = 0
    init_vel = 5

    snake_size = 15
    food_size = 15
    fps=50

    while not exit_game:

        if game_over:
            gameWindow.fill(black)
            text_screen("Ooopsss!! Game Over!!! Press Enter To Continue ||  Score: " + str(score*5), red, 130, 220)

            for event in pg.event.get():

                if event.type == pg.QUIT:
                    exit_game = True

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        GameLoop()

        else:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit_game = True

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        vel_x = init_vel
                        vel_y = 0

                    if event.key == pg.K_LEFT:
                        vel_x = -init_vel
                        vel_y = 0

                    if event.key == pg.K_UP:
                        vel_x = 0
                        vel_y = -init_vel

                    if event.key == pg.K_DOWN:
                        vel_x = 0
                        vel_y = init_vel

                    
            snake_x += vel_x
            snake_y += vel_y

            #Food eat
            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                score +=1
                food_x = random.randint(10, screen_width/1.5)
                food_y = random.randint(10, screen_height/1.5)
                snake_length += 3 

            #main screen
            gameWindow.fill(black)
            gameWindow.blit(bg_img,(0,0))
            text_screen("Score: " + str(score * 5), (255,255,0), screen_width/2, 5)
            pg.draw.circle(gameWindow, red, (food_x, food_y),7)

            #To start
            snake_head = []
            snake_head.append(snake_x)
            snake_head.append(snake_y)
            snake_list.append(snake_head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            #Game Over
            #collision with itself
            if snake_head in snake_list[:-1]:
                game_over= True
            
            #collision with walls
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True

            #pg.draw.rect(gameWindow, green, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow,green,snake_list,snake_size)

        pg.display.update()
        clock.tick(fps)

    pg.quit()
    quit()

GameLoop()


    