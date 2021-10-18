import pygame
import time
import random


difficulty = 10

win_x = 720
win_y = 480

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

c = [red, blue, green]

total = []

pygame.init()

pygame.display.set_caption('Navs snake')
game_win = pygame.display.set_mode((win_x, win_y))

fps = pygame.time.Clock()

#Score control
def score_disp(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surf = score_font.render("score: " + str(score), True, color)
    score_rect = score_surf.get_rect()
    game_win.blit(score_surf, score_rect)

#Ending the game
def game_over():
    game_win.fill(black)
    myfont = pygame.font.SysFont('times new roman', 40)
    intro_surface = 'Thank you for playing'
    textcolor = red
    blitlines(game_win, intro_surface, myfont, textcolor, win_x/5, win_y/4)
    time.sleep(2)
    pygame.quit()
    quit()

def blitlines(surf, text, renderer, color, x, y):
    h = renderer.get_height()
    lines = text.split('\n')
    for i, ll in enumerate(lines):
        txt_surface = renderer.render(ll, True, color)
        surf.blit(txt_surface, (x, y+(i*h)))
        pygame.display.flip()

#Intro screen and getting difficulty
def intro_display():
    global difficulty
    game_win.fill(black)
    myfont = pygame.font.SysFont('times new roman', 40)
    intro_surface = 'Please select difficulty \n1. Easy \n2. Medium \n3. Hard'
    textcolor = white
    blitlines(game_win, intro_surface, myfont, textcolor, win_x/5, win_y/4)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    difficulty = 10
                    game()
                if event.key == pygame.K_2:
                    difficulty = 15
                    game()
                if event.key == pygame.K_3:
                    difficulty = 20
                    game()

#For continuing or exiting the game
def continue_screen():
    game_win.fill(black)
    myfont = pygame.font.SysFont('times new roman', 30)
    score_font = pygame.font.SysFont('times new roman', 50)
    scr_a = 'Score: ' + str(score)
    play_a = 'DO YOU WANT TO PLAY AGAIN \ny: YES \nn: NO'
    blitlines(game_win, scr_a, score_font, red, win_x/3, win_y/6)
    blitlines(game_win, play_a, myfont, white, win_x/5, win_y/3)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    intro_display()
                if event.key == pygame.K_n:
                    game_over()


#Game control
def game():
    s_pos = [100, 50]
    S_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]]

    f_pos = [random.randrange(1, (win_x//10))*10, random.randrange(1, (win_y//10))*10]
    f_spawn = True

    direction = 'RIGHT'
    change_to = direction

    global score
    score = 0

    while True:
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
                if event.key == pygame.K_DELETE:
                    continue_screen()

        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            s_pos[1] -= 10
        if direction == 'DOWN':
            s_pos[1] += 10
        if direction == 'LEFT':
            s_pos[0] -= 10
        if direction == 'RIGHT':
            s_pos[0] += 10

        if s_pos[0] < 0:
            s_pos[0] += win_x
        if s_pos[0] > win_x-10:
            s_pos[0] -= win_x
        if s_pos[1] < 0:
            s_pos[1] += win_y
        if s_pos[1] > win_y-10:
            s_pos[1] -= win_y

        S_body.insert(0, list(s_pos))
        if s_pos[0] == f_pos[0] and s_pos[1] == f_pos[1]:
            score += 1
            f_spawn = False
        else:
            S_body.pop()

        if f_spawn != True:
            f_pos = [random.randrange(1, (win_x//10))*10, random.randrange(1, (win_y//10))*10]
        
        f_spawn = True
        game_win.fill(black)

        for i in S_body:
            pygame.draw.rect(game_win, random.choice([red, blue, green]), pygame.Rect(i[0], i[1], 10, 10))
        pygame.draw.rect(game_win, white, pygame.Rect(f_pos[0], f_pos[1], 10, 10))

        for snake in S_body[1:]:
            if s_pos[0] == snake[0] and s_pos[1] == snake[1]:
                total.append(score)
                continue_screen()

        score_disp(white, 'times new roman', 20)

        pygame.display.update()
        fps.tick(difficulty)

intro_display()
