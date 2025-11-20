import pygame
import os
pygame.init()

screen = pygame.display.set_mode((1080, 800))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

#Colors
RED = (230, 0, 0)
GREEN = (0, 230, 0)
BLUE = (0, 0, 230)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (230, 230, 0)
CYAN = (0, 230, 230)
MAGENTA = (230, 0, 230)
colors = [RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA]
color = WHITE

screen.fill(BLACK)

eraser = pygame.image.load('eraser.png')
eraser = pygame.transform.scale(eraser, (70, 70))

mode = "circle"  

def draw_palette():
    for i, c in enumerate(colors):
        pygame.draw.rect(screen, c, (i * 40, 0, 40, 40))
    #rectangle,circle, eraser buttons
    pygame.draw.rect(screen, WHITE, (260, 0, 40, 40), 2)  # rect button
    pygame.draw.circle(screen, WHITE, (340, 20), 18, 2)   # circle button
    screen.blit(eraser, (1010, 0))  # eraser button

def pick_tool(x, y):
    global color, mode
    if 0 <= y <= 40:
        if 0 <= x <= 240:          # палитра цветов
            index = x // 40
            color = colors[index]
            mode = "circle"
        elif 260 <= x <= 300:      # прямоугольник
            mode = "rect"
        elif 320 <= x <= 360:      # круг
            mode = "circle"
        elif 1010 <= x <= 1080:    # ластик
            mode = "eraser"

def paint(x, y):
    if mode == "circle":
        pygame.draw.circle(screen, color, (x, y), 15)
    elif mode == "rect":
        pygame.draw.rect(screen, color, (x - 20, y - 20, 40, 40))
    elif mode == "eraser":
        pygame.draw.circle(screen, BLACK, (x, y), 30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if y <= 40:
                pick_tool(x, y)

        elif event.type == pygame.KEYDOWN:
            #выбрать фигуры нажимая на первую букву с англ 
            if event.key == pygame.K_r:
                mode = "rect"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_e:
                mode = "eraser"
            # когда нажимаю на х экран полностью чистый, удаляется все данные
            elif event.key == pygame.K_x:
                screen.fill(BLACK)
            # how to choose color by number, press from 1 to 6, сверху цифры нужно нажать с намклок не работало
            elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6]:
                index = event.key - pygame.K_1
                if index < len(colors):
                    color = colors[index]
                    mode = "circle"

#рисовать 
    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        if y > 40:
            paint(x, y)

    draw_palette()
    pygame.display.update()
    clock.tick(120)

pygame.quit()