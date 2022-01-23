import pygame

class Ball():
    
    def __init__(self, screen):
        '''initialization'''
        self.screen = screen
        self.image = pygame.image.load("py_test.png")       #load image
        self.image.set_colorkey((255,255,255))              #delete white in image
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.centerx = 120                             #start koordination x
        self.rect.centery = 120                             #start koordination y

    def output(self):
        '''draw object'''
        self.screen.blit(self.image, self.rect)
        
    def move(self, step, move_x, w, h):
        '''move ball up - down '''
        self.rect.centerx += move_x
        self.rect.centery += step

def work_position(ball, R, W, H, right, move_x, step, start_speed,
                  MUL_SLOW, acceleration, flag, up):
    ''' this function handles object's position and change his speed and acceleration '''
    next_color = 0
    if (ball.rect.centerx - R < 0 and right):  #check touch left border and change speed
        move_x = -move_x - 1
        right = False
        next_color += 1
    if ball.rect.centerx + R >= W and not right:    #check touch right border and change speed
        move_x = -move_x + 1
        right = True
        next_color += 1
    if (ball.rect.centery - R <= 0 and up): #check up border and change direction of moving
        step = -step
        next_color += 1
        up = False
    if (ball.rect.centery + R >= H):    #check down border and change direction of moving

        flag = True
        up = True
        step = -start_speed
        start_speed -= acceleration*MUL_SLOW
        next_color += 1
        
    if (ball.rect.centerx <= R and step == 0): #check stop object, no change in koordination y
        move_x = 0   
    if (H - ball.rect.centery - R - abs(step)> 0 or abs(move_x) >= 1): #check down border or change in x
        ball.move(step, move_x, W, H)
    if flag:    #if touch down border
        step += acceleration
    return right, move_x, step, start_speed, flag, next_color, up

def screen_update(screen, ball, cur_color, next_color, Color, TIME_TO_DRAW, MODUL_COLOR):
    cur_color = (cur_color + next_color)% MODUL_COLOR
    screen.fill(Color[cur_color])
    ball.output()   #draw object
    pygame.time.delay(TIME_TO_DRAW)
    pygame.display.update()
    return cur_color
