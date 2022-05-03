from colorsys import rgb_to_hls, rgb_to_hsv
from ctypes.wintypes import RGB
import pygame
import random

pygame.init()
WIDTH, HEIGHT = 1400, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("partitek by bennyBoy")
clock = pygame.time.Clock()     ## For syncing the FPS
FPS = 60

BLACK, WHITE = (0, 0, 0), (255, 255, 255)

class Ball:
    def __init__(self, start_x, start_y, left_right, up_down, speed_x, speed_y, size, color):
        self.x = start_x
        self.y = start_y
        self.speedx = speed_x
        self.speedy = speed_y
        self.lr = left_right
        self.ud = up_down
        self.size = size
        self.color = color
        self.lifespan = random.randint(1,50)
        self.weight = 0


def ball_coords(x, y, lr, ud, ball_speedx, ball_speedy, ball_size, ball_weight):
    R = ball_size

    if lr:
        x += ball_speedx
    else:
        x -= ball_speedx
    
    if ud:
        y += ball_speedy + round(ball_weight)
    else:
        y -= ball_speedy - round(ball_weight)

    if x <= R or x >= (WIDTH - R):
        if lr:
            lr = False
        else:
            lr = True
    if y <= R or y >= (HEIGHT - R):
        if ud:
            ud = False
        else:
            ud = True

    ball_weight += 1
    return x, y, lr, ud, ball_weight


def draw_ball(x, y, size, color):
    pygame.draw.circle(screen, color, (x, y), size, 2)


def get_mouse_coords():
    return pygame.mouse.get_pos()


def fader(r, g, b):

    if r >= menu.fadeSpeed:
        r -= menu.fadeSpeed
    else:
        r = 0
    if g >= menu.fadeSpeed:
        g -= menu.fadeSpeed
    else:
        g = 0
    if b >= menu.fadeSpeed:
        b -= menu.fadeSpeed
    else:
        b = 0
    return r, g, b

class Menu:
    def __init__(self):
        self.background = pygame.Rect(WIDTH - 200, 0, WIDTH, HEIGHT)
        self.background_color = (50, 50, 50)
        self.quantity = 1000
        self.flow = 150
        self.maxSize = 50
        self.fadeSpeed = 5
        self.quantity_slider = pygame.Rect(WIDTH - 180, (HEIGHT // 5), 160, 1)
        self.flow_slider = pygame.Rect(WIDTH - 180, (HEIGHT // 5) * 2, 160, 1)
        self.maxSize_slider = pygame.Rect(WIDTH - 180, (HEIGHT // 5) * 3, 160, 1)
        self.fadeSpeed_slider = pygame.Rect(WIDTH - 180, (HEIGHT // 5) * 4, 160, 1)
        self.quantity_switch = pygame.Rect((WIDTH - 180) + ((160 / 1000) * self.quantity), (HEIGHT // 5), 20, 20)
        self.flow_switch = pygame.Rect((WIDTH - 180) + ((160 / 200) * self.flow), ((HEIGHT // 5) * 2), 20, 20)
        self.maxSize_switch = pygame.Rect((WIDTH - 180) + ((160 / 200) * self.maxSize), ((HEIGHT // 5) * 3), 20, 20)
        self.fadeSpeed_switch = pygame.Rect((WIDTH - 180) + ((160 / 50) * self.fadeSpeed), ((HEIGHT // 5) * 4), 20, 20)
        
    
    def draw_background(self):
        pygame.draw.rect(screen, self.background_color, self.background, 1, 20)

    def draw_sliders(self):
        sliders = [self.quantity_slider, self.flow_slider, self.maxSize_slider, self.fadeSpeed_slider]
        for slider in sliders:
            pygame.draw.rect(screen, (150, 150, 150), slider)

        switches = [self.quantity_switch, self.flow_switch, self.maxSize_switch, self.fadeSpeed_switch]
        switch_coords = [((WIDTH - 180) + ((160 / 1000) * self.quantity), (HEIGHT // 5)),
                         ((WIDTH - 180) + ((160 / 200) * self.flow), ((HEIGHT // 5) * 2)),
                         ((WIDTH - 180) + ((160 / 200) * self.maxSize), ((HEIGHT // 5) * 3)),
                         ((WIDTH - 180) + ((160 / 50) * self.fadeSpeed), ((HEIGHT // 5) * 4)),
                        ]

        for idx, switch in enumerate(switches):
            switch.center = switch_coords[idx]
            pygame.draw.rect(screen, WHITE, switch, 1)

    def move_sliders(self, x, y):

        # limits:
        quantity = range(1, 1001)
        flow = range(1, 201)
        maxSize = range(1, 51)
        fadeSpeed = range(21)


        switch_coords = [((WIDTH - 180) + ((160 / 1000) * self.quantity), (HEIGHT // 5)),
                         ((WIDTH - 180) + ((160 / 200) * self.flow), ((HEIGHT // 5) * 2)),
                         ((WIDTH - 180) + ((160 / 50) * self.maxSize), ((HEIGHT // 5) * 3)),
                         ((WIDTH - 180) + ((160 / 50) * self.fadeSpeed), ((HEIGHT // 5) * 4)),
                        ]
        #switch_coords[0][0]
        mouse_down = False
        current = 0
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if ((WIDTH - 180 - 10) <= x <= (WIDTH - 180 + 160 + 10)) and ((HEIGHT // 5) - 10) <= y <= ((HEIGHT // 5) + 10):
                mouse_down = True
                if mouse_down:
                    current = x - (WIDTH - 180)
                    if 0 < current <= 160:
                        self.quantity = round((current / 160) * 1000)
            elif ((WIDTH - 180 - 10) <= x <= (WIDTH - 180 + 160 + 10)) and (((HEIGHT // 5) * 2) - 10) <= y <= (((HEIGHT // 5) * 2) + 10):
                mouse_down = True
                if mouse_down:
                    current = x - (WIDTH - 180)
                    if 0 < current <= 160:
                        self.flow = round((current / 160) * 200)
            elif ((WIDTH - 180 - 10) <= x <= (WIDTH - 180 + 160 + 10)) and (((HEIGHT // 5) * 3) - 10) <= y <= (((HEIGHT // 5) * 3) + 10):
                mouse_down = True
                if mouse_down:
                    current = x - (WIDTH - 180)
                    if 0 < current <= 160:
                        self.maxSize = round((current / 160) * 200)
            elif ((WIDTH - 180 - 10) <= x <= (WIDTH - 180 + 160 + 10)) and (((HEIGHT // 5) * 4) - 10) <= y <= (((HEIGHT // 5) * 4) + 10):
                mouse_down = True
                if mouse_down:
                    current = x - (WIDTH - 180)
                    if 0 < current <= 160:
                        self.fadeSpeed = round((current / 160) * 50)
            
def menu_labels():
    font_style_text = "./Montserrat-VariableFont_wght.ttf"
    font_style_title = "./AlegreyaSansSC-Light.ttf"

    label = pygame.font.Font(font_style_text, 15)
    title = pygame.font.Font(font_style_title, 35)

    title_surface = title.render("partitek", True, (255,127,80))
    label_surface1 = label.render("POPULATION", True, WHITE)
    label_surface2 = label.render("BANDWIDTH", True, WHITE)
    label_surface3 = label.render("DIMENSION LIMIT", True, WHITE)
    label_surface4 = label.render("FADER RATE", True, WHITE)

    title_surface_rect = title_surface.get_rect()
    label_surface1_rect = label_surface1.get_rect()
    label_surface2_rect = label_surface2.get_rect()
    label_surface3_rect = label_surface3.get_rect()
    label_surface4_rect = label_surface4.get_rect()

    title_surface_rect.center = ((WIDTH - 100), (HEIGHT // 5) // 5)
    label_surface1_rect.x, label_surface1_rect.y = (WIDTH - 180), (HEIGHT // 5 + 15)
    label_surface2_rect.x, label_surface2_rect.y = (WIDTH - 180), (((HEIGHT // 5) * 2) + 15)
    label_surface3_rect.x, label_surface3_rect.y = (WIDTH - 180), (((HEIGHT // 5) * 3) + 15)
    label_surface4_rect.x, label_surface4_rect.y = (WIDTH - 180), (((HEIGHT // 5) * 4) + 15)

    screen.blit(title_surface, title_surface_rect)
    screen.blit(label_surface1, label_surface1_rect)
    screen.blit(label_surface2, label_surface2_rect)
    screen.blit(label_surface3, label_surface3_rect)
    screen.blit(label_surface4, label_surface4_rect)

balls = []
menu = Menu()

## Game loop
running = True
while running:

    #1 Process input/events
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False

   
    screen.fill(BLACK)
    
    x, y = get_mouse_coords()

    if 0 < x < (WIDTH - 200) and 0 < y < HEIGHT:
        pygame.mouse.set_visible(False)
    else:
        pygame.mouse.set_visible(True)

    if x > 0 and (x + (menu.maxSize // 2)) < (WIDTH - 200) and y > 0 and (y + (menu.maxSize // 2)) < HEIGHT:
        on_screen, menu_screen = True, False
    elif (WIDTH - 200) < x < WIDTH and 0 < y < HEIGHT:
        on_screen, menu_screen = False, True
    else:
        on_screen, menu_screen = False, False


    if len(balls) < menu.quantity and any([on_screen, menu_screen]):
        for ball in range(menu.quantity):
            size = random.randint(1, menu.maxSize)
            if on_screen:
                x, y = get_mouse_coords()
            elif menu_screen:
                x, y = (WIDTH - 200) // 2, HEIGHT // 2
            #start_x, start_y, left_right, up_down, speed_x, speed_y, size, color
            ball = Ball(x, y, 
            random.choice([0, 1]), random.choice([0, 1]), random.randint(1, 20), random.randint(1, 20), size,
            (100, 0, random.randint(1, 255)))
            balls.append(ball)
            if len(balls) % menu.flow == 0:
                break


    for ball in balls:
        ball.lifespan -= 1
        if ball.lifespan < 1:
            balls.remove(ball)
        draw_ball(ball.x, ball.y, ball.size, ball.color)
        ball.color = fader(*ball.color)
        ball.x, ball.y, ball.lr, ball.ud, ball.weight = ball_coords(ball.x, ball.y, ball.lr, ball.ud, ball.speedx, ball.speedy, ball.size, ball.weight)


    menu.draw_background()
    menu.draw_sliders()
    menu.move_sliders(*get_mouse_coords())
    menu_labels()
    pygame.display.flip()       

pygame.quit()
