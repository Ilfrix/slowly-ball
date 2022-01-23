import sys
import pygame, objects
from ball_vars import *
from objects import Ball


def run():
    global W, H, TIME_TO_DRAW, Color, step, R, move_x, start_speed,\
    acceleration, MUL_SLOW, flag, right, cur_color, next_color, up,\
    MODUL_COLOR

    #functions
    pygame.init()
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("BALL")
    ball = Ball(screen)
    #main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #closing window after click X
                pygame.quit()
                sys.exit()
        right, move_x, step, start_speed, flag, next_color, up =\
        objects.work_position(ball, R, W, H, right, move_x, step,
                              start_speed, MUL_SLOW, acceleration, flag, up)
        cur_color = objects.screen_update(screen, ball, cur_color,
                               next_color, Color, TIME_TO_DRAW, MODUL_COLOR)
                
run()
