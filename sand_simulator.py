import pygame
import sys
import random

pygame.init()

is_sand_udpated : bool = False
is_running : bool = True
is_mouse_down : bool = False
mouse_pos : list = [-1, -1]

screen_width : int = 600
screen_height : int = 400
hueValue : int = 1
 
sand_size : int = 4

brush_size : int = 2

x_limit : int = int(screen_width / sand_size)
y_limit : int = int(screen_height / sand_size)

canvas = [[0 for i in range(y_limit)] for j in range(x_limit)]

# color = 194, 178, 128

def draw_sand(x, y):
    i = x * sand_size
    j = y * sand_size
    
    pygame.draw.rect(surface, (255, canvas[x][y], 128), (i, j, sand_size, sand_size))

def add_sand(x, y):
    global is_sand_udpated

    x = int(x / sand_size)
    y = int(y / sand_size)

    for i in range(x - brush_size, x + brush_size, 1):
        for j in range(y - brush_size, y + brush_size, 1):
            if i < 0 or i >= x_limit or j < 0 or j >= y_limit: continue
            canvas[i][j] = hueValue
            is_sand_udpated = True

def update_sand():
    global is_sand_udpated

    for x in range(x_limit - 1, -1, -1):
        for y in range(y_limit - 2, -1, -1):
            if(canvas[x][y] != 0 and canvas[x][y + 1] == 0):
                canvas[x][y], canvas[x][y + 1] = 0, canvas[x][y]
                is_sand_udpated = True
            elif(canvas[x][y] != 0 and x + 1 < x_limit and canvas[x + 1][y + 1] == 0 and random.randrange(0, 10) >= 5):
                canvas[x][y], canvas[x + 1][y + 1] = 0, canvas[x][y]
                is_sand_udpated = True
            elif(canvas[x][y] != 0 and x - 1 >= 0 and canvas[x - 1][y + 1] == 0):
                canvas[x][y], canvas[x - 1][y + 1] = 0, canvas[x][y]
                is_sand_udpated = True

def update_input():
    global is_running
    global is_mouse_down
    global mouse_pos
    global canvas

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            canvas = [[0 for i in range(y_limit)] for j in range(x_limit)]
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_mouse_down = True
            mouse_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            is_mouse_down = False
            mouse_pos = [-1, -1]
        elif event.type == pygame.MOUSEMOTION and is_mouse_down:
            mouse_pos = event.pos

surface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Falling Sand Simulation DEMO")

surface.fill((255, 255, 255))
pygame.display.flip()

while is_running:
    hueValue += 0.2
    
    if hueValue > 255: hueValue = 0

    update_sand()
    update_input()

    if is_mouse_down: add_sand(mouse_pos[0], mouse_pos[1])

    if not is_sand_udpated: continue
    
    surface.fill((255, 255, 255))

    for x in range(x_limit):
        for y in range(y_limit):
            if canvas[x][y] != 0:
                draw_sand(x, y)

    pygame.display.flip()

pygame.quit()
sys.exit()