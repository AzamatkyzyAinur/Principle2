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


#palette sverhu
def draw_palette():
    # color buttons
    for i, c in enumerate(colors):
        pygame.draw.rect(screen, c, (i * 40, 0, 40, 40))

    #круг
    pygame.draw.circle(screen, WHITE, (340, 20), 18, 2)

    #прямоугольник
    pygame.draw.rect(screen, WHITE, (260, 10, 30, 20), 2)

    #квадрат
    pygame.draw.rect(screen, WHITE, (390, 10, 20, 20), 2)

    #прямой треугольник
    pygame.draw.polygon(screen, WHITE, [(440, 30), (440, 10), (460, 30)], 2)

    #равносторонний треугольник
    pygame.draw.polygon(screen, WHITE, [(500, 10), (485, 30), (515, 30)], 2)

    #ромб
    pygame.draw.polygon(screen, WHITE,
                        [(550, 5), (535, 20), (550, 35), (565, 20)], 2)

    #eraser
    screen.blit(eraser, (1010, 0))


def pick_tool(x, y):
    global color, mode
    if 0 <= y <= 40:
        if x < 240:  #палитра цветов
            index = x // 40
            color = colors[index]
            mode = "circle"

        elif 260 <= x <= 300:
            mode = "rect"

        elif 320 <= x <= 360:
            mode = "circle"

        elif 380 <= x <= 420:
            mode = "square"

        elif 430 <= x <= 470:
            mode = "right_triangle"

        elif 480 <= x <= 520:
            mode = "equilateral_triangle"

        elif 530 <= x <= 570:
            mode = "rhombus"

        elif x >= 1010:
            mode = "eraser"


def paint(x, y):
    if mode == "circle":
        pygame.draw.circle(screen, color, (x, y), 20)

    elif mode == "rect":
        pygame.draw.rect(screen, color, (x - 30, y - 20, 60, 40))

    elif mode == "square":
        pygame.draw.rect(screen, color, (x - 25, y - 25, 50, 50))

    elif mode == "right_triangle":
        pygame.draw.polygon(screen, color,
                            [(x, y - 30), (x, y + 30), (x + 30, y + 30)])

    elif mode == "equilateral_triangle":
        pygame.draw.polygon(screen, color,
                            [(x, y - 35), (x - 30, y + 20), (x + 30, y + 20)])

    elif mode == "rhombus":
        pygame.draw.polygon(screen, color,
                            [(x, y - 30), (x - 30, y), (x, y + 30), (x + 30, y)])

    elif mode == "eraser":
        pygame.draw.circle(screen, BLACK, (x, y), 35)



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
            if event.key == pygame.K_x:
                screen.fill(BLACK)

            #change color 1–6 палетка
            elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3,
                               pygame.K_4, pygame.K_5, pygame.K_6]:
                index = event.key - pygame.K_1
                if index < len(colors):
                    color = colors[index]
                    mode = "circle"

            #выбрать фигуры первая буква
            elif event.key == pygame.K_r:
                mode = "rect"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_e:
                mode = "eraser"

    #painting with mouse
    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        if y > 40:
            paint(x, y)

    draw_palette()
    pygame.display.update()
    clock.tick(120)

pygame.quit()