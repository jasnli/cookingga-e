import pygame
from food import Food
from button import Button
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
buttons = [Button("start.png", 833, 550), Button("make_steak_button.png", 500, 500)]

### NOTE FOR SELF ###
### MAKE A NEW SCREEN FOR SELECTION LATER ON ###

## TEXTURES TEMPORARY:
# COOKED_STEAK, START, BACKGROUND, FREEZER


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
select_screen = False

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
move_1 = False
move_other_object = True
selection_made = False
cooking = False
# -------- Main Program Loop -----------
while run:
    clock.tick(60)

    # if selection_made:
    #     start = True
    # --- Main event loop
    ## ----- NO BLIT ZONE START ----- ##
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        # mouse coordinates
        if event.type == pygame.MOUSEMOTION:
            mouse_position = pygame.mouse.get_pos()
            mouse_position_text = temporary_font.render(str(mouse_position), True, (0, 0, 0))
        if event.type == pygame.MOUSEBUTTONDOWN and buttons[0].rect.collidepoint(event.pos):
            select_screen = True
        if select_screen:
            if event.type == pygame.MOUSEBUTTONDOWN and buttons[1].rect.collidepoint(event.pos):
                cooking = True
                select_screen = False


            # SPAWN STEAK
        if cooking:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    for i in range(1):
                        steak = Food("steak", mouse_position[0] - 128, mouse_position[1] - 128)
                        foods.append(steak)


            if len(foods) > 0:
            # CHOPPING (TEMP)
                for s in foods:
                    if event.type == pygame.MOUSEBUTTONDOWN and s.rect.collidepoint(event.pos):
                        if event.button == 2:
                            print(s.chop_number)
                            s.chop_food()
                            s.update_photo()

            # COOKING (TEMP)
                for s in foods:
                    if event.type == pygame.MOUSEBUTTONDOWN and s.rect.collidepoint(event.pos):
                        if event.button == 3:
                            s.cooked = True
                            s.update_photo()

            # DRAGGING OBJECT CHANGE THIS LATER
            if len(foods) > 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        move_1 = True
                if move_1:
                    for s in foods:
                        if s.rect.collidepoint(event.pos) and move_other_object:
                            move = True
                            moved_object = s
                            move_other_object = False
                        if move:
                            moved_object.move_food((mouse_position[0] - moved_object.image_size[0] / 2, mouse_position[1] - moved_object.image_size[0] / 2))
                            moved_object.update_photo()
                        if event.type == pygame.MOUSEBUTTONUP:
                            if event.button == 1:
                                move = False
                                move_1 = False
                                move_other_object = True


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
    if not select_screen and not cooking:
        screen.blit(buttons[0].image, buttons[0].rect)
        screen.blit(title_screen_msg, (550, 250))
    if select_screen:
        screen.blit(buttons[1].image, buttons[1].rect)

    # start [TEMP]
    if cooking:
        if len(foods) > 0:
            for i in foods:
                screen.blit(i.image, i.rect)
        if select_screen:
            print("")

    screen.blit(mouse_position_text, mouse_position)
    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()




