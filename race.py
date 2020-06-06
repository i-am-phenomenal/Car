import pygame
import time
import random 

screen_width = 800
screen_height = 600 
black_color_rgb = (0,0,0)

pygame.init()
grey = (119,118, 110)
game_display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Race")
clock= pygame.time.Clock()
car_image = pygame.image.load(r"C:/python_game/images/car_2.png")
green_background = pygame.image.load(r"C:/python_game/images/green_background.jpg")
yellow_strip = pygame.image.load(r"C:/python_game/images/yellow strip.jpg")
white_strip = pygame.image.load(r"C:/python_game/images/white_strip.jpg")
car_width = 50


def render_background(): 
    game_display.blit(green_background, (0,0))
    game_display.blit(green_background, (0, 200))
    game_display.blit(green_background, (0, 400))
    game_display.blit(green_background, (700, 0))
    game_display.blit(green_background, (700, 200))
    game_display.blit(green_background, (700, 400))
    game_display.blit(yellow_strip, (400, 0))
    game_display.blit(yellow_strip, (400, 100))
    game_display.blit(yellow_strip, (400, 200))
    game_display.blit(yellow_strip, (400, 300))
    game_display.blit(yellow_strip, (400, 400))
    game_display.blit(yellow_strip, (400, 500))
    game_display.blit(white_strip, (120,0))
    game_display.blit(white_strip, (120,100))
    game_display.blit(white_strip, (120,200))
    game_display.blit(white_strip, (680,0))
    game_display.blit(white_strip, (680,100))
    game_display.blit(white_strip, (680,200))
    

def render_car(x_coor, y_coor):
    print((x_coor, y_coor))
    game_display.blit(car_image, (x_coor, y_coor))

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

def car_crash():
    display_message("YOU CRASHED")

def render_obstacle(x_coord, y_coord, obs): 


def game_loop(): 
    x_coord = (screen_width * 0.45)
    y_coord = (screen_height * 0.8)
    obstacle_speed = 0.8
    obs = 0
    y_delta = 0
    obs_start_x_cord = random.randrange(200, (screen_width - 200))
    obs_start_y_coord = -750
    obs_width = 56
    obs_height = 12
    x_delta = 0

    crashed = False  

    while not crashed: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                crashed = True 

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT: 
                    x_delta -= 0.8

            if event.key == pygame.K_RIGHT:
                    x_delta += 0.8

        if event.type ==pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                x_delta = 0

        x_coord += x_delta 
        game_display.fill(grey)
        render_background()
        obs_start_y_coord= (obstacle_speed / 4)
        render_obstacle(obs_start_x_coord, obs_start_y_coord, obs)
        obs_start_y_coord += obstacle_speed
        render_car(x_coord, y_coord)
        if x_coord > 680 - car_width or x_coord < 110: 
            car_crash()
        pygame.display.update()    
        clock.tick(60)
