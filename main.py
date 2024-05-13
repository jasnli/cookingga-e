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
### NOTE FOR SELF ###
### MAKE A NEW SCREEN FOR SELECTION LATER ON ###

# foods creation
steak = Food("steak", 100, 100)

# start button
start_button = pygame.image.load("start.png")
start_button = pygame.transform.scale(start_button, (228, 92))

# [TEMP] mouse position
mouse_position = (0, 0)

# set up variables for the display
SCREEN_HEIGHT = 1020
SCREEN_WIDTH = 1920
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

# VARIABLE FOR START
start = False

# render the text for later
title_message = "COOKING GAME" #CHANGE NAME LATER
title_screen_msg = title_font.render(title_message, True, (114, 189, 53))
# [TEMP] mouse pos text
mouse_position_text = temporary_font.render(str(mouse_position), True, (0, 0, 0))




# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:


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

        # TEMPORARY COOKING
        # if event.type == pygame.MOUSEBUTTONDOWN and steak.rect.collidepoint(event.pos):
        #     steak.cooked = True
        #     steak.update_photo()

        # TEMPORARY CUT
        if event.type == pygame.MOUSEBUTTONDOWN and steak.rect.collidepoint(event.pos):
            steak.chop_food()
            print(steak.image_size)



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
        screen.blit(steak.image, steak.rect)

    ### test
    origin1 = (0, 0)
    separation = 20


    width, height = steak.image_size[0] / 2, steak.image_size
    origin2 = origin1[0] + width + separation, origin1[1]

    # Blit first half
    source_area = pygame.Rect((0, 0), (width, height))
    screen.blit(steak.rect, origin1, source_area)

    # Blit second half
    source_area = pygame.Rect((width, 0), (width, height))
    screen.blit(steak.rect, origin2, source_area)

    screen.blit(mouse_position_text, mouse_position)
    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()




