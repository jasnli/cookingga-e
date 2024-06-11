import pygame
from food import Food
from button import Button
from customer import Customer
from kitchen_apps import Appliance
import random
import time


# set up pygame modules
pygame.init()
pygame.font.init()
title_font = pygame.font.SysFont('curlz', 120)
title_font.set_bold(True)
temporary_font = pygame.font.SysFont('Arial', 40)
temp_big_font = pygame.font.SysFont('Arial', 100)
pygame.display.set_caption("KITCHEN COOKING")
# background
bg = pygame.image.load("background.jpg")

# BUTTONS
# 0 = Start, 1 = Start Cooking, 2 = Back, 3 = Serve
buttons = [Button("start.png", 5000, 5000, (57 * 4, 23 * 4)), Button("start_cooking_button.png", 1300, 200, (612 / 1.25, 408 / 1.25)), Button("back_button.png", 10, 10, (256, 128))]

inventory_button = Button("inventory.png", 1400, 600, (300, 200))

cutting_board = Button("cutting_board.png", 9399, 5950, (17 * 15, 24 * 15))
serve_overlay_button = Button("serve_overlay.png", 9933, 8378, (52 * 5, 20 * 5))
plate = Food("plate", 9383, 9292)
bowl = Food("bowl", 8492, 9834)
knife = Button("knife.png", 9439, 8192, (25 * 10, 27 * 10))
salt_shaker = Food("salt", 8342, 8492)

# APPLIANCES
# 0 = Stove, 1 = Frying Pan
appliance_buttons = [Appliance("stove", 5000, 5000), Appliance("frying_pan", 8000, 6000)]
stove_images = ["stove_on_1.png", "stove_on_2.png", "stove_on_3.png", "stove_off.png"]
knife_image = pygame.image.load("knife.png")
knife_image = pygame.transform.scale(knife_image, (128, 128))
knife_image = pygame.transform.rotate(knife_image, 45)
knife_image_size = knife_image.get_size()
# BASKETS FOR THE FOOD
lettuce_basket = Button("lettuce_basket.png", 8000, 8900, (33 * 5, 36 * 5))
carrot_basket = Button("carrot_basket.png", 7000, 8900, (23 * 5, 36 * 5))
steak_table = Button("steak_table.png", 8500, 8900, (65 * 5, 18 * 5))
bread_table = Button("bread_table.png", 9999, 9999, (65 * 5, 51 * 5))

# TRASH CAM
trash_can = Button("trash.png", 9000, 9000, (15 * 10, 22 * 10))

# HOVER DISPLAYS
stove_hover_display = pygame.image.load("stove_hover_text.png")
carrot_hover_display = pygame.image.load("carrot_hover_text.png")
lettuce_hover_display = pygame.image.load("lettuce_hover_text.png")
steak_hover_display = pygame.image.load("steak_hover_text.png")
bread_hover_display = pygame.image.load("bread_hover_text.png")
bread_hover_display = pygame.transform.scale(bread_hover_display, (29 * 5, 14 * 5))


# RECEIPT

receipt = pygame.image.load("receipt.png")
order_cooked_steak_whole = pygame.image.load("whole_cooked_steak.png")
order_cooked_steak_whole = pygame.transform.scale(order_cooked_steak_whole, (256, 256))
order_fruit_salad = pygame.image.load("fruit_salad.png")
order_fruit_salad = pygame.transform.scale(order_fruit_salad, (256, 256))
order_caesar_salad = pygame.image.load("caesar_salad.png")
order_caesar_salad = pygame.transform.scale(order_caesar_salad, (256, 256))
order_milkshake = pygame.image.load("milkshake.png")
order_milkshake = pygame.transform.scale(order_milkshake, (256, 256))
order_orange_juice = pygame.image.load("orange_juice.png")
order_orange_juice = pygame.transform.scale(order_orange_juice, (256, 256))
order_soda = pygame.image.load("soda.png")
order_soda = pygame.transform.scale(order_soda, (256, 256))
order_water = pygame.image.load("water.png")
order_water = pygame.transform.scale(order_water, (256, 256))
empty_text = title_font.render("", True, (114, 189, 53))
main_order = [empty_text, order_cooked_steak_whole] #INDEX : 0 = COMPLETED, 1 = WHOLE
side_order = [empty_text, order_fruit_salad, order_caesar_salad] #INDEX : 0 = COMPLETED, 1 = FRUIT, 2 = CAESAR
drinks_order = [empty_text, order_soda, order_orange_juice, order_water, order_milkshake] #INDEX : 0 = COMPLETED, 1 = SODA, 2 = OJ, 3 = WATER, 4 = MILKSHAKE
display_foods = [order_cooked_steak_whole, order_fruit_salad, order_caesar_salad, order_milkshake, order_orange_juice, order_water, order_soda]



# [TEMP] mouse position
mouse_position = (0, 0)


temporary_position = 0

# set up variables for the display
SCREEN_HEIGHT = 1020
SCREEN_WIDTH = 1920
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

# customer maker
customer = Customer(SCREEN_HEIGHT)
customer_pics = ["customer_1.png", "customer_2.png", "customer_3.png"]
# foods creation
foods = []
made_mains = [0] # INDEX 0 = WHOLE
made_sides = [0, 0] # INDEX 0 = FRUIT, INDEX 1 = CAESAR
made_drinks = [0, 0, 0, 0] # INDEX 0 = SODA, INDEX 1 = OJ, INDEX 2 = WATER, INDEX 3 = MILKSHAKE


cooked_steak_display_num = title_font.render(str(made_mains[0]), True, (255, 50, 50))
caesar_salad_display_num = title_font.render(str(made_sides[1]), True, (255, 50, 50))
fruit_salad_display_num = title_font.render(str(made_sides[0]), True, (255, 50, 50))
soda_display_num = title_font.render(str(made_drinks[0]), True, (255, 50, 50))
oj_display_num = title_font.render(str(made_drinks[1]), True, (255, 50, 50))
water_display_num = title_font.render(str(made_drinks[2]), True, (255, 50, 50))
milkshake_display_num = title_font.render(str(made_drinks[3]), True, (255, 50, 50))
display_inventory_amounts = [cooked_steak_display_num, caesar_salad_display_num, fruit_salad_display_num,
                             soda_display_num, oj_display_num, water_display_num, milkshake_display_num]

# VARIABLE FOR SCREENS
start_screen = True
select_screen = False
cooking = False
appliance_selection = False
stove_screen = False
inventory = False

# VARIABLES FOR HOVER
stove_hover_on = False
carrot_hover_on = False
lettuce_hover_on = False
steak_hover_on = False
bread_hover_on = False

# render the text for later
title_message = "KITCHEN COOKING"
title_screen_msg = title_font.render(title_message, True, (114, 189, 53))
temporary_text = temp_big_font.render("ALL SPRITES ARE TEMPORARY AS PLACEHOLDERS", True, (114, 189, 53))
# [TEMP] mouse pos text
mouse_position_text = temporary_font.render(str(mouse_position), True, (0, 0, 0))

# frame
frame = 0
clock = pygame.time.Clock()


# actions
run = True
move = False
move_1 = False
move_other_object = True
selection_made = False
show_mouse_coordinates = False
frozen_overlay_screen = False
food_being_served = ""
valid_entry = False
temporary_frame = 10000
temporary_frozen_overlay_position = (0, 0)
add_cookedness = True
cutting_mode = False
salt_stays = True


valid_entry_main = False
valid_entry_side = False
valid_entry_drink = False
new_order = False
ordered = False
# -------- Main Program Loop -----------
while run:
    clock.tick(60)

    if frame == temporary_frame + 60:
        serve_overlay_button.update_image("serve_overlay.png", (52 * 5, 20 * 5))

    # COOKING & BURNING
    if len(foods) > 0:
        for s in foods:
            s.update_photo()
            if pygame.Rect.colliderect(s.rect, appliance_buttons[1].rect):
                if frame % 30 == 0:
                    s.cookedness += 10
                    print(s.cookedness)
                if 160 <= s.cookedness < 240:
                    s.cooked = True
                    s.update_photo()
                if s.cookedness >= 240:
                    s.burnt = True
                    s.update_photo()

    # NEW ORDER
    if new_order:
        random_customer_image = random.randint(0, 2)
        customer.customer_updater(customer_pics[random_customer_image])
        customer.random_order()
        print(customer.order)
        new_order = False
        ordered = True


    # FOR ANIMATION FOR STOVE
    if appliance_buttons[0].stove_on:
        if frame % 10 == 0:
            appliance_buttons[0].stove_animation_pic += 1
        if appliance_buttons[0].stove_animation_pic > 2:
            appliance_buttons[0].stove_animation_pic = 0
        appliance_buttons[0].update_photo(stove_images[appliance_buttons[0].stove_animation_pic])

        # SPAWNING FRYING PAN AFTER STOVE IS TURNED ON
        appliance_buttons[1].x, appliance_buttons[1].y = 1000, 100
        appliance_buttons[1].update_pos()
    else:
        appliance_buttons[0].stove_animation_pic = 3
        appliance_buttons[0].update_photo(stove_images[appliance_buttons[0].stove_animation_pic])
        appliance_buttons[1].x, appliance_buttons[1].y = 8000, 6000
        appliance_buttons[1].update_pos()

    # --- Main event loop
    ## ----- NO BLIT ZONE START ----- ##
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        # mouse coordinates
        if event.type == pygame.MOUSEMOTION:
            mouse_position = pygame.mouse.get_pos()
            mouse_position_text = temporary_font.render(str(mouse_position), True, (0, 0, 0))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m and not show_mouse_coordinates:
                show_mouse_coordinates = True
            elif event.key == pygame.K_m and show_mouse_coordinates:
                show_mouse_coordinates = False
        # BUTTON TO START
        if start_screen:
            buttons[0].x, buttons[0].y = 833, 550
            buttons[0].update_button()
            if event.type == pygame.MOUSEBUTTONDOWN and buttons[0].rect.collidepoint(event.pos):
                select_screen = True
                new_order = True
                start_screen = False
                buttons[0].x, buttons[0].y = 5000, 5000
                buttons[0].update_button()
        # BUTTON TO COOK OR INVENTORY
        if select_screen:
            if event.type == pygame.MOUSEBUTTONDOWN and buttons[1].rect.collidepoint(event.pos):
                cooking = True
                appliance_selection = True
                select_screen = False
                new_order = False
            if event.type == pygame.MOUSEBUTTONDOWN and inventory_button.rect.collidepoint(mouse_position):
                select_screen = False
                inventory = True

        # INVENTORY UPDATING
        if inventory:
            cooked_steak_display_num = title_font.render(str(made_mains[0]), True, (255, 50, 50))
            caesar_salad_display_num = title_font.render(str(made_sides[1]), True, (255, 50, 50))
            fruit_salad_display_num = title_font.render(str(made_sides[0]), True, (255, 50, 50))
            soda_display_num = title_font.render(str(made_drinks[0]), True, (255, 50, 50))
            oj_display_num = title_font.render(str(made_drinks[1]), True, (255, 50, 50))
            water_display_num = title_font.render(str(made_drinks[2]), True, (255, 50, 50))
            milkshake_display_num = title_font.render(str(made_drinks[3]), True, (255, 50, 50))
            display_inventory_amounts = [cooked_steak_display_num, fruit_salad_display_num, caesar_salad_display_num,
                                         soda_display_num, oj_display_num, water_display_num, milkshake_display_num]

            if event.type == pygame.MOUSEBUTTONDOWN and buttons[2].rect.collidepoint(
                    event.pos):  # BACK BUTTON TO CUSTOMER SCREEN
                if event.button == 1:
                    select_screen = True
                    cooking = False
                    inventory = False


        # COOKING STUFF BELOW

        # APPLIANCE SELECTION SCREEN
        if cooking:

            trash_can.x, trash_can.y = SCREEN_WIDTH - trash_can.image_size[0], SCREEN_HEIGHT - trash_can.image_size[1]
            trash_can.update_button()



            if appliance_selection:
                appliance_buttons[0].x, appliance_buttons[0].y = 400, SCREEN_HEIGHT - appliance_buttons[0].image_size[1] # PUTS STOVE IN FRAME
                appliance_buttons[0].update_pos()
                if event.type == pygame.MOUSEBUTTONDOWN and buttons[2].rect.collidepoint(event.pos):    # BACK BUTTON TO CUSTOMER SCREEN
                    if event.button == 1:
                        select_screen = True
                        cooking = False

                if appliance_buttons[0].rect.collidepoint(mouse_position):
                    stove_hover_on = True
                    if event.type == pygame.MOUSEBUTTONDOWN:    # TAKES YOU TO STOVE SCREEN
                        if event.button == 1:
                            stove_screen = True
                            appliance_selection = False
                else:
                    stove_hover_on = False


            # STOVE SCREEN
            if stove_screen:
                # MOVING EVERYTHING INTO FRAME
                plate.x, plate.y = SCREEN_WIDTH - plate.image_size[0] - 200, 200
                plate.update_photo()
                bowl.x, bowl.y = SCREEN_WIDTH - bowl.image_size[0] - 200, 500
                bowl.update_photo()
                appliance_buttons[0].x, appliance_buttons[0].y = 400, SCREEN_HEIGHT - appliance_buttons[0].image_size[1]  # PUTS STOVE IN FRAME
                appliance_buttons[0].update_pos()
                cutting_board.x, cutting_board.y = 420, 220 # CUTTING BOARD IN FRAME
                cutting_board.update_button()
                knife.x, knife.y = cutting_board.x - 300, cutting_board.y
                knife.update_button()

                carrot_basket.x, carrot_basket.y = 422 + appliance_buttons[0].image_size[0], SCREEN_HEIGHT - carrot_basket.image_size[1] # CARROT TABLE IN FRAME
                carrot_basket.update_button()
                lettuce_basket.x, lettuce_basket.y = 422 + appliance_buttons[0].image_size[0] + carrot_basket.image_size[0], SCREEN_HEIGHT - lettuce_basket.image_size[1] # LETTUCE TABLE IN FRAME
                lettuce_basket.update_button()
                steak_table.x, steak_table.y = 400 + appliance_buttons[0].image_size[0], SCREEN_HEIGHT - carrot_basket.image_size[1] - steak_table.image_size[1] # STEAK TABLE IN FRAME
                steak_table.update_button()
                bread_table.x, bread_table.y = steak_table.x + steak_table.image_size[0], SCREEN_HEIGHT - bread_table.image_size[1] # BREAD TABLE IN FRAME
                bread_table.update_button()

                # MOVING THE SALT SHAKER
                if salt_stays:
                    salt_shaker.x, salt_shaker.y = 100, 800
                    salt_shaker.update_photo()
                elif not salt_stays:
                    salt_shaker.x, salt_shaker.y = mouse_position[0] - salt_shaker.image_size[0] / 2, mouse_position[1] - salt_shaker.image_size[1] / 2
                    salt_shaker.update_photo()

                if salt_shaker.rect.collidepoint(mouse_position):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        salt_stays = False
                    if event.type == pygame.MOUSEBUTTONUP:
                        salt_stays = True

                # CUTTING ANIMATION
                if knife.rect.collidepoint(mouse_position):
                    if event.type == pygame.MOUSEBUTTONDOWN and not cutting_mode:
                        cutting_mode = True
                        knife.update_image("knife_highlighted.png", (25 * 10, 27 * 10))
                    elif event.type == pygame.MOUSEBUTTONDOWN and cutting_mode:
                        cutting_mode = False
                        knife.update_image("knife.png", (25 * 10, 27 * 10))

                # STOVE ACTION
                if appliance_buttons[0].rect.collidepoint(mouse_position):
                    if not appliance_buttons[0].stove_on:
                        if event.type == pygame.MOUSEBUTTONUP:  ## TURNS STOVE ON
                            if event.button == 3:
                                appliance_buttons[0].stove_on = True
                    elif appliance_buttons[0].stove_on:
                        if event.type == pygame.MOUSEBUTTONUP:  ## TURNS STOVE OFF
                            if event.button == 3:
                                appliance_buttons[0].stove_on = False

                # HOVERS
                if carrot_basket.rect.collidepoint(mouse_position): # HOVERING CARROT
                    carrot_hover_on = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for i in range(1):
                            carrot = Food("carrot", mouse_position[0], mouse_position[1])
                            foods.append(carrot)
                else:
                    carrot_hover_on = False

                if lettuce_basket.rect.collidepoint(mouse_position): # HOVERING LETTUCE
                    lettuce_hover_on = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for i in range(1):
                            lettuce = Food("lettuce", mouse_position[0] - 128, mouse_position[1] - 128)
                            foods.append(lettuce)
                else:
                    lettuce_hover_on = False

                if steak_table.rect.collidepoint(mouse_position): # HOVERING STEAK
                    steak_hover_on = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for i in range(1):
                            steak = Food("steak", mouse_position[0] - 128, mouse_position[1] - 128)
                            foods.append(steak)
                else:
                    steak_hover_on = False

                if bread_table.rect.collidepoint(mouse_position): # HOVERING BREAD
                    bread_hover_on = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for i in range(1):
                            bread = Food("bread", mouse_position[0] - 128, mouse_position[1] - 128)
                            foods.append(bread)
                else:
                    bread_hover_on = False

                if event.type == pygame.MOUSEBUTTONDOWN and buttons[2].rect.collidepoint(event.pos): ## BACK BUTTON TO APPLIANCE SCREEN
                    if event.button == 1:
                        appliance_selection = True
                        stove_screen = False
                        appliance_buttons[0].stove_on = False

            else: # MOVE THEM AWAY
                carrot_basket.x, carrot_basket.y = 8100, 8100
                lettuce_basket.x, lettuce_basket.y = 8200, 8200
                steak_table.x, steak_table.y = 8300, 8300
                bread_table.x, bread_table.y = 9999, 8923
                cutting_board.x, cutting_board.y = 9383, 5110 # CUTTING BOARD IN FRAME
                cutting_board.update_button()
                knife.x, knife.y = 8458, 8392
                knife.update_button()


            # RIGHT CLICK OVERLAY (SERVE BUTTON)
            if frozen_overlay_screen:
                serve_overlay_button.x, serve_overlay_button.y = temporary_frozen_overlay_position[0], temporary_frozen_overlay_position[1]
                serve_overlay_button.update_button()
                if event.type == pygame.MOUSEBUTTONDOWN and not serve_overlay_button.rect.collidepoint(mouse_position):
                    frozen_overlay_screen = False

                if serve_overlay_button.rect.collidepoint(mouse_position):
                    serve_overlay_button.update_image("serve_hover_overlay.png", (52 * 5, 20 * 5))
                else:
                    serve_overlay_button.update_image("serve_overlay.png", (52 * 5, 20 * 5))

                # UPDATING INV
                if event.type == pygame.MOUSEBUTTONDOWN and serve_overlay_button.rect.collidepoint(mouse_position):
                    if food_being_served.food_name == "whole_cooked_steak":
                        made_mains[0] = made_mains[0] + 1
                        valid_entry_main = True
                        valid_entry = True
                    if food_being_served.food_name == "fruit_salad":
                        made_sides[0] = made_sides[0] + 1
                        valid_entry_side = True
                        valid_entry = True
                    if food_being_served.food_name == "caesar_salad":
                        made_sides[1] = made_sides[1] + 1
                        valid_entry_side = True
                        valid_entry = True
                    if food_being_served.food_name == "soda":
                        made_drinks[0] = made_drinks[0] + 1
                        valid_entry_drink = True
                        valid_entry = True
                    if food_being_served.food_name == "oj":
                        made_drinks[1] = made_drinks[1] + 1
                        valid_entry_drink = True
                        valid_entry = True
                    if food_being_served.food_name == "water":
                        made_drinks[2] = made_drinks[2] + 1
                        valid_entry_drink = True
                        valid_entry = True
                    if food_being_served.food_name == "milkshake":
                        made_drinks[3] = made_drinks[3] + 1
                        valid_entry_drink = True
                        valid_entry = True

                    if valid_entry:
                        if valid_entry_main:
                            plate.food_name = "plate"
                            frozen_overlay_screen = False
                            print(made_mains, made_sides, made_drinks)
                            valid_entry = False
                            valid_entry_main = False

                        if valid_entry_side:
                            bowl.food_name = "bowl"
                            frozen_overlay_screen = False
                            print(made_mains, made_sides, made_drinks)
                            valid_entry = False
                            valid_entry_side = False

                    else:
                        temporary_frame = frame
                        serve_overlay_button.update_image("serve_error_overlay.png", (52 * 5, 20 * 5))
                        valid_entry = False

            else:
                serve_overlay_button.x, serve_overlay_button.y = 9483, 8409
                serve_overlay_button.update_button()
                valid_entry = False

            # ADDING SALT TO BOWL
            if pygame.Rect.colliderect(salt_shaker.rect, bowl.rect):
                if bowl.food_name == "caesar_salad_no_salt":
                    print(bowl.food_name)
                    bowl.food_name = "caesar_salad"
                    bowl.combination()
                    salt_stays = True

            if len(foods) > 0 and not frozen_overlay_screen:

                for s in foods:
                    # PLATE
                    if pygame.Rect.colliderect(s.rect, plate.rect):
                        print(s.food_name)
                        if s.food_name == "cooked_steak":
                            plate.food_name = "plate_with_steak"
                            plate.combination()
                            foods.remove(s)
                        if s.food_name == "chopped_carrot_3" and plate.food_name == "plate_with_steak":
                            plate.food_name = "whole_steak_with_carrots"
                            plate.combination()
                            foods.remove(s)
                        if s.food_name == "chopped_lettuce_3" and plate.food_name == "plate_with_steak":
                            plate.food_name = "whole_steak_with_lettuce"
                            plate.combination()
                            foods.remove(s)
                        if s.food_name == "chopped_carrot_3" and plate.food_name == "whole_steak_with_lettuce":
                            plate.food_name = "whole_cooked_steak"
                            plate.combination()
                            foods.remove(s)
                        if s.food_name == "chopped_lettuce_3" and plate.food_name == "whole_steak_with_carrots":
                            plate.food_name = "whole_cooked_steak"
                            plate.combination()
                            foods.remove(s)

                    if pygame.Rect.colliderect(s.rect, bowl.rect):
                        if s.food_name == "chopped_lettuce_3" and bowl.food_name == "bowl":
                            bowl.food_name = "lettuce_bowl"
                            bowl.combination()
                            foods.remove(s)
                        if s.food_name == "croutons" and bowl.food_name == "lettuce_bowl":
                            bowl.food_name = "caesar_salad_no_salt"
                            bowl.combination()
                            foods.remove(s)

                    # CUTTING
                    if pygame.Rect.colliderect(s.rect, cutting_board.rect):
                        s.cuttable = True
                    else:
                        s.cuttable = False

                    if s.cuttable and cutting_mode:
                        if s.rect.collidepoint(mouse_position) and event.type == pygame.MOUSEBUTTONDOWN:
                            s.chop_food()
                            s.update_photo()

                        # OVERLAY FEATURED
                    if event.type == pygame.MOUSEBUTTONDOWN and s.rect.collidepoint(mouse_position):
                        if event.button == 3:
                            frozen_overlay_screen = True
                            food_being_served = s
                            temporary_frozen_overlay_position = mouse_position
                            move_1 = False
                            move = False


                    # TRASH FEATURE
                    if pygame.Rect.colliderect(s.rect, trash_can.rect):
                        foods.remove(s)

            if event.type == pygame.MOUSEBUTTONDOWN and plate.rect.collidepoint(mouse_position):
                if event.button == 3:
                    frozen_overlay_screen = True
                    food_being_served = plate
                    temporary_frozen_overlay_position = mouse_position
                    move_1 = False
                    move = False

            if event.type == pygame.MOUSEBUTTONDOWN and bowl.rect.collidepoint(mouse_position):
                if event.button == 3:
                    frozen_overlay_screen = True
                    food_being_served = bowl
                    temporary_frozen_overlay_position = mouse_position
                    move_1 = False
                    move = False

            # DRAGGING OBJECT CHANGE THIS LATER
            if event.type == pygame.MOUSEBUTTONUP:
                move_other_object = True
            if len(foods) > 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        move_1 = True
                if move_1 and not cutting_mode:
                    for f in foods:
                        if f.rect.collidepoint(mouse_position) and move_other_object and s.food_type != "plate":
                            move = True
                            moved_object = f 
                            move_other_object = False
                        if move and not frozen_overlay_screen:
                            moved_object.move_food((mouse_position[0] - moved_object.image_size[0] / 2, mouse_position[1] - moved_object.image_size[0] / 2))
                            moved_object.update_photo()
                        if event.type == pygame.MOUSEBUTTONUP and not frozen_overlay_screen:
                            if event.button == 1:
                                move = False
                                move_1 = False
                else:
                    move_other_object = True

        else:
            appliance_buttons[0].x, appliance_buttons[0].y = 8000, 8000  # PUTS STOVE IN FRAME
            appliance_buttons[0].update_pos()

    ##  ----- NO BLIT ZONE END  ----- ##

    ## FILL SCREEN, and BLIT here ##
    # start screen
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    if start_screen:
        screen.blit(buttons[0].image, buttons[0].rect)
        screen.blit(title_screen_msg, (550, 250))
    if select_screen:
        # customer

        screen.blit(temporary_text, (50, 100))
        screen.blit(receipt, (customer.image_size[0] + 50, SCREEN_HEIGHT - receipt.get_size()[1] - 100))
        screen.blit(customer.customer_image, customer.rect)
        screen.blit(buttons[1].image, buttons[1].rect)
        screen.blit(inventory_button.image, inventory_button.rect)
        if ordered:
            screen.blit(main_order[customer.order[0]], (710, 200))
            screen.blit(side_order[customer.order[1]], (710, 200 + 256))
            screen.blit(drinks_order[customer.order[2]], (710, 200 + 256 + 256))

    if inventory:
        screen.blit(buttons[2].image, buttons[2].rect)
        temporary_position = 0
        for i in range(len(display_foods)):
            screen.blit(display_foods[i], (temporary_position, 200))
            screen.blit(display_inventory_amounts[i], (temporary_position + 70, 500))


            temporary_position += 250
    # start [TEMP]
    if cooking:
        screen.blit(trash_can.image, trash_can.rect)
        screen.blit(buttons[2].image, buttons[2].rect)

        if appliance_selection:
            screen.blit(appliance_buttons[0].image, appliance_buttons[0].rect)
            if stove_hover_on:
                screen.blit(stove_hover_display, mouse_position)


        if stove_screen:
            screen.blit(plate.image, plate.rect)
            screen.blit(bowl.image, bowl.rect)
            screen.blit(knife.image, knife.rect)
            screen.blit(appliance_buttons[0].image, appliance_buttons[0].rect)
            screen.blit(carrot_basket.image, carrot_basket.rect)
            screen.blit(lettuce_basket.image, lettuce_basket.rect)
            screen.blit(steak_table.image, steak_table.rect)
            screen.blit(bread_table.image, bread_table.rect)
            screen.blit(cutting_board.image, cutting_board.rect)
            if carrot_hover_on:
                screen.blit(carrot_hover_display, mouse_position)
            if lettuce_hover_on:
                screen.blit(lettuce_hover_display, mouse_position)
            if steak_hover_on:
                screen.blit(steak_hover_display, mouse_position)
            if bread_hover_on:
                screen.blit(bread_hover_display, mouse_position)
            if appliance_buttons[0].stove_on:
                screen.blit(appliance_buttons[1].image, appliance_buttons[1].rect)
            if len(foods) > 0:
                for i in foods:
                    screen.blit(i.image, i.rect)
            if cutting_mode:
                screen.blit(knife_image, (mouse_position[0] - knife_image_size[0] / 2, mouse_position[1] -knife_image_size[0] / 2))
            screen.blit(salt_shaker.image, salt_shaker.rect)
        if frozen_overlay_screen:
            screen.blit(serve_overlay_button.image, serve_overlay_button.rect)

    frame += 1

    if show_mouse_coordinates:
        screen.blit(mouse_position_text, mouse_position)
    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()




