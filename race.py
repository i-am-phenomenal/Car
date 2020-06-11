import pygame
import time
import random
import os 

screen_width = 800
screen_height = 600 
black_color_rgb = (0,0,0)
bright_green_rgb = (0, 255, 0)
red_color_rgb = (255,0,0)
green_color_rgb = ( 0, 200, 0)
grey = (119,118, 110)
paused = False
current_images_dir = os.getcwd() + "/images/"

pygame.init()
game_display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Race")
clock= pygame.time.Clock()
car_image = pygame.image.load(current_images_dir + "car_2.png")
green_background = pygame.image.load(current_images_dir + "green_background.jpg")
yellow_strip = pygame.image.load(current_images_dir + "yellow strip.jpg")
white_strip = pygame.image.load(current_images_dir + "white_strip.jpg")
intro_background = pygame.image.load(current_images_dir + "intro_background.jpg")
instruction_background = pygame.image.load(current_images_dir + "instruction_background.jpg")
car_width = 50
cars_passed = 0
level = 0 
score = 0


def render_button(message, x,y,w,h,ic,ac, action=None): 
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w> mouse[0] > x and (y + h) > mouse[1] > y: 
        pygame.draw.rect(game_display, ac, (x,y,w,h))
        if click[0] == 1 and action != None: 
            print(action, "ACTION: ")
            if action == "Play": 
                counter = True
                while counter: 
                    for event in pygame.event.get(): 
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                            sys.exit()

                    # game_loop()
                # game_loop()

            elif action == "Quit":
                pygame.quit()
                quit()
                sys.exit()

    else: 
        pygame.draw.rect(game_display, ic, (x,y,w,h))

    small_text = pygame.font.Font("freesansbold.ttf", 20)
    text_surface, text_rect = text_objects(message, small_text)
    text_rect.center = ((x + (w/2)), (y + (h/2)))
    game_display.blit(text_surface, text_rect)

def intro_loop(): 
    intro = True 

    while intro:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()
                sys.exit()

        game_display.blit(intro_background, (0, 0))
        pygame.display.update()
        clock.tick(50)
        large_text = pygame.font.Font("freesansbold.ttf", 115)
        TextSurf, TextRect = text_objects("Needy for Speed",large_text)
        TextRect.center = (400, 100)
        game_display.blit(TextSurf, TextRect)
        render_button("Start", 150, 520, 100, 50, green_color_rgb, bright_green_rgb, "Play")
        pygame.display.update()
        clock.tick(50)

def render_obstacle(x_coord, y_coord, obs): 
    absolute_path = r"C:/python_game/images/"

    if obs == 0: 
        image_name = "obs_1.jpg"
    else: 
        image_name = "obs_" + str(obs) + ".jpg"

    image_path = absolute_path + image_name
    obs_image = pygame.image.load(image_path)

    game_display.blit(obs_image, (x_coord, y_coord))


def render_car(x_coor, y_coor):
    game_display.blit(car_image, (x_coor, y_coor))


def render_score_board(cars_passed, current_score): 
    font = pygame.font.Font("freesansbold.ttf", 14)
    cars_passed = font.render(("Cars Passed: " + str(cars_passed)), True, red_color_rgb)
    current_score = font.render(("Score: " + str(current_score)), True, black_color_rgb)
    game_display.blit(cars_passed, (0,30))
    game_display.blit(current_score, (0, 50))


def text_objects(text, font):
    text_surface = font.render(text, True, black_color_rgb)
    return text_surface, text_surface.get_rect()

def display_message(text): 
    large_text = pygame.font.Font("freesansbold.ttf", 80)
    text_surface, text_rect = text_objects(text, large_text)
    text_rect.center = ((screen_width / 2), (screen_height / 2))
    game_display.blit(text_surface, text_rect)
    pygame.display.update()
    time.sleep(3)
    game_loop()

def update_high_score(): 
    global score
    file_score = 0
    current_directory = os.getcwd()
    file_path = current_directory + "/score.txt"
    try: 
        with open(file_path, "r") as file: 
            data = file.readlines()
            file.close()
            file_score = int(data[0])

        if score > file_score: 
            with open(file_path, "w") as score_file: 
                score_file.write(str(score))
                score_file.close()

    except Exception as e: 
        print(e)
        print("File does not exist")
        print("creating new score file")
        
        with open(file_path, "w") as score_file: 
            score_file.write(str(score))
            score_file.close()

def car_crash():
    update_high_score()
    display_message("YOU CRASHED")

# Issue => you have to double tap the "c" key to unpause
def pause_game(): 
    global paused

    while paused: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_c: 
                    paused = False

                elif event.key == pygame.K_q: 
                    pygame.quit()
                    quit()

        pause_text = pygame.font.SysFont('Consolas', 32).render('Game Paused', True, pygame.color.Color('White'))
        pause_help_text = pygame.font.SysFont('Consolas', 16).render('Press c to Continue or q to Quit', True, pygame.color.Color('White'))
        game_display.fill(black_color_rgb)
        game_display.blit(pause_text, (320, 300))
        game_display.blit(pause_help_text, (320, 350))
        pygame.display.update()
        clock.tick(5)

def countdown():
    countdown = True
    
    while countdown:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            game_display.fill(grey)
            move_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("3",largetext)
            TextRect.center=((screen_width/2),(screen_height/2))
            game_display.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            game_display.fill(grey)
            move_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("2",largetext)
            TextRect.center=((screen_width/2),(screen_height/2))
            game_display.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            game_display.fill(grey)
            move_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("1",largetext)
            TextRect.center=((screen_width/2),(screen_height/2))
            game_display.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            game_display.fill(grey)
            move_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("GO!!!",largetext)
            TextRect.center=((screen_width/2),(screen_height/2))
            game_display.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            game_loop()

def game_loop(): 
    global paused 
    global cars_passed
    global score
    x_coord = (screen_width * 0.45)
    y_coord = (screen_height * 0.8)
    obstacle_speed = 9
    obs = 0
    y_delta = 0
    obs_start_x_coord = random.randrange(200, (screen_width - 200))
    obs_start_y_coord = -750
    obs_width = 56
    obs_height = 125
    x_delta = 0
    y2 = 7
    crashed = False  

    while not crashed: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                           
                pygame.quit()
                quit()

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT: 
                    x_delta -= 0.8

            if event.key == pygame.K_RIGHT:
                    x_delta += 0.8  

            if event.key == pygame.K_p: 
                paused = True

            if event.key == pygame.K_r: 
                paused = False

            if event.key == pygame.K_UP: 
                obstacle_speed += 2

            if event.key == pygame.K_DOWN: 
                obstacle_speed -= 2
     
        if event.type ==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                x_delta = 0

        x_coord += x_delta 
        game_display.fill(grey)

        rel_y =  y2 % green_background.get_rect().width
        game_display.blit(green_background, (0, rel_y - green_background.get_rect().width))
        game_display.blit(green_background, (700, rel_y - green_background.get_rect().width))

        if rel_y < 800: 
            game_display.blit(green_background, (0, rel_y))
            game_display.blit(green_background, (700, rel_y))
            game_display.blit(yellow_strip, (400, rel_y))
            game_display.blit(yellow_strip, (400, rel_y + 100))
            game_display.blit(yellow_strip, (400, rel_y + 200))
            game_display.blit(yellow_strip, (400, rel_y + 300))
            game_display.blit(yellow_strip, (400, rel_y + 400))
            game_display.blit(yellow_strip, (400, rel_y + 500))
            game_display.blit(yellow_strip, (400, rel_y - 100))
            game_display.blit(white_strip, (120, rel_y - 200))
            game_display.blit(white_strip, (120, rel_y + 20))
            game_display.blit(white_strip, (120, rel_y + 30))
            game_display.blit(white_strip, (680, rel_y - 100))
            game_display.blit(white_strip, (680, rel_y + 20))
            game_display.blit(white_strip, (680, rel_y + 30))
        
        y2 += obstacle_speed

        obs_start_y_coord -= (obstacle_speed / 4)
        render_obstacle(obs_start_x_coord, obs_start_y_coord, obs)

        obs_start_y_coord += obstacle_speed
        render_car(x_coord, y_coord)

        render_score_board(cars_passed, score)

        if paused: 
            pause_game()         

        if x_coord > 680 - car_width or x_coord < 110: 
            car_crash()

        if x_coord > (screen_width - (car_width + 110)) or x_coord < 110: 
            car_crash()

        if obs_start_y_coord > screen_height:
            cars_passed += 1
            score = cars_passed * 5
            obs_start_y_coord = 0 - obs_height
            obs_start_x_coord = random.randrange(170, (screen_width - 170))
            obs = random.randrange(0, 7)

        if y_coord < obs_start_y_coord + obs_height: 
            if x_coord > obs_start_x_coord and x_coord < obs_start_x_coord + obs_width or x_coord + car_width > obs_start_x_coord and x_coord + car_width < obs_start_x_coord + obs_width: 
                car_crash()

        pygame.display.update()    
        clock.tick(60)
