import pygame
from food import Food
import random
import time


# set up pygame modules
pygame.init()
pygame.font.init()
title_font = pygame.font.SysFont('curlz', 120)
title_font.set_bold(True)
temporary_font = pygame.font.SysFont('Arial', 40)
pygame.display.set_caption("COOKING GAME [CHANGE NAME LATER]")
# background
bg = pygame.image.load("background.jpg")
# BUTTONS
start_button = pygame.image.load("start.png")
start_button = pygame.transform.scale(start_button, (228, 92))

market_button = pygame.image.load("market.png")

temporary_button = pygame.image.load("temporary.png")
### NOTE FOR SELF ###
### MAKE A NEW SCREEN FOR SELECTION LATER ON ###

## TEXTURES TEMPORARY:
# COOKED_STEAK, START, BACKGROUND


# foods creation
foods = []


# [TEMP] mouse position
mouse_position = (0, 0)

# set up variables for the display
SCREEN_HEIGHT = 1020
SCREEN_WIDTH = 1920
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

# VARIABLE FOR SCREENS
start = False
market = False

# render the text for later
title_message = "COOKING GAME" #CHANGE NAME LATER
title_screen_msg = title_font.render(title_message, True, (114, 189, 53))
# [TEMP] mouse pos text
mouse_position_text = temporary_font.render(str(mouse_position), True, (0, 0, 0))

# frame
frame = 0
clock = pygame.time.Clock()


# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
move = False

# -------- Main Program Loop -----------
while run:
    clock.tick(60)


    # --- Main event loop
    ## ----- NO BLIT ZONE START ----- ##
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        # mouse coordinates
        if event.type == pygame.MOUSEMOTION:
            mouse_position = pygame.mouse.get_pos()
            mouse_position_text = temporary_font.render(str(mouse_position), True, (0, 0, 0))
        if event.type == pygame.MOUSEBUTTONDOWN and 833 < mouse_position[0] < 833 + start_button.get_size()[0] and 550 < mouse_position[1] < start_button.get_size()[1] + 550:
            start = True

        # SPAWN STEAK
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                for i in range(1):
                    steak = Food("steak", mouse_position[0] - 128, mouse_position[1] - 128)
                    foods.append(steak)

        # TEMPORARY COOKING
        if len(foods) > 0:
            for s in foods:
                if event.type == pygame.MOUSEBUTTONDOWN and i.rect.collidepoint(event.pos):
                    s.cooked = True
                    s.update_photo()

        # DRAGGING OBJECT CHANGE THIS LATER
        if len(foods) > 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    move = True
                for s in foods:
                    print('hi')
                    if s.rect.collidepoint(event.pos):
                        move = True
        if move:
            s.move_food((mouse_position[0] - s.image_size[0] / 3, mouse_position[1] - s.image_size[0] / 3))
            s.update_photo()
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                move = False


        # MARKET SCREEN
        # if start and not market:
        #     if pygame.MOUSEBUTTONDOWN and 100 < mouse_position < 100 + market_button.get_size[0] # CONTINUE NEXT
        #         print('.')
        #         market = True
        #
        # if start and market: # CONTINUE NEXT


    ##  ----- NO BLIT ZONE END  ----- ##

    ## FILL SCREEN, and BLIT here ##
    # start screen
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    if not start:
        screen.blit(start_button, (833, 550))
        screen.blit(title_screen_msg, (550, 250))

    # start [TEMP]
    if start:
        if len(foods) > 0:
            for i in foods:
                screen.blit(i.image, i.rect)
        # if not market:
        #     screen.blit()

    screen.blit(mouse_position_text, mouse_position)
    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()




