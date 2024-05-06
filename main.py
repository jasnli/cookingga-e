import pygame
import random
import time

# set up pygame modules
pygame.init()
pygame.font.init()
title_font = pygame.font.SysFont('centaur', 120)
pygame.display.set_caption("COOKING GAME [CHANGE NAME LATER]")
for i in pygame.font.get_fonts():
    print(i)
# background
bg = pygame.image.load("background.jpg")

# set up variables for the display
SCREEN_HEIGHT = 1020
SCREEN_WIDTH = 1920
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)


r = 50
g = 0
b = 100

# render the text for later
message = "TEST TITLE MESSAGE"
display_message = title_font.render(message, True, (255, 255, 255))


# Instantiate the apple

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:


    # --- Main event loop
    ## ----- NO BLIT ZONE START ----- ##
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    ##  ----- NO BLIT ZONE END  ----- ##

    ## FILL SCREEN, and BLIT here ##
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    screen.blit(display_message, (150, 250))
    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()





