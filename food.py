import pygame


def set_photo_and_resize(photo, size):
    image = pygame.image.load(photo)
    image = pygame.transform.scale(image, size)
    return image


def rect_updater(picture_size, picture, x, y, rectangle, image_picture, size):
    picture = set_photo_and_resize(image_picture, size)
    picture_size = picture.get_size()
    rectangle = pygame.Rect(x, y, picture_size[0], picture_size[1])
    return rectangle, picture_size, picture


class Food:
    def __init__(self, food_type, x, y):
        self.food_type = food_type
        self.cooked = False
        self.burnt = False
        self.x = x
        self.y = y
        self.chop_number = 0
        self.movable = True
        self.cookedness = 0
        self.image_size = (0, 0)
        self.food_name = ""
        self.cuttable = False

        if food_type == "bread":
            self.image = set_photo_and_resize("bread.png", (256, 256))
            self.image_size = self.image.get_size()
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
            self.food_name = "bread"

        if food_type == "salt":
            self.image = set_photo_and_resize("salt.png", (256, 256))
            self.image_size = self.image.get_size()
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
            self.food_name = "salt"

        if food_type == "plate":
            self.image = set_photo_and_resize("plate.png", (256, 256))
            self.image_size = self.image.get_size()
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
            self.food_name = "plate"

        if food_type == "bowl":
            self.image = set_photo_and_resize("bowl.png", (256, 256))
            self.image_size = self.image.get_size()
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
            self.food_name = "bowl"

        if food_type == "steak":  # STEAK
            self.cooking_stage = 0
            if not self.cooked:
                self.image = set_photo_and_resize("raw_steak.png", (256, 256))
                self.image_size = self.image.get_size()
                self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
                self.food_name = "raw_steak"

        if food_type == "carrot":  # CARROT
            self.image = set_photo_and_resize("carrot.png", (256, 256))
            self.image_size = self.image.get_size()
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
            self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "carrot.png", (256, 256))
            self.food_name = "unchopped_carrot"

        if food_type == "lettuce":  # LETTUCE
            self.image = set_photo_and_resize("lettuce.png", (256, 256))
            self.image_size = self.image.get_size()
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
            self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "lettuce.png", (256, 256))
            self.food_name = "unchopped_lettuce"

        # TEMPORARY
        if food_type == "whole_cooked_steak":
            self.image = set_photo_and_resize("whole_cooked_steak.png", (256, 256))
            self.image_size = self.image.get_size()
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
            self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "whole_cooked_steak.png", (256, 256))
            self.food_name = "whole_cooked_steak"

    def update_photo(self):
        if self.food_type == "plate" and self.food_name == "plate":
            self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "plate.png", (256, 256))

        if self.food_type == "bowl" and self.food_name == "bowl":
            self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "bowl.png", (256, 256))

        if self.food_type == "bread":
            if self.chop_number == 0 and not self.cooked:
                self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "bread.png", (256, 256))
                self.food_name = "bread"
            if self.chop_number > 0 and not self.cooked:
                self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "cut_bread.png", (256, 256))
                self.food_name = "cut_bread"
            if self.chop_number == 0 and self.cooked:
                self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "toast.png", (256, 256))
                self.food_name = "toast"
            if self.chop_number > 0 and self.cooked:
                self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "croutons.png", (256, 256))
                self.food_name = "croutons"


        if self.food_type == "steak" and self.food_type != "plate":
                if not self.cooked:
                    self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "raw_steak.png", (256, 256))
                    self.food_name = "raw_steak"
                if self.cooked and not self.burnt:
                    self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "cooked_steak.png", (256, 256))
                    self.food_name = "cooked_steak"
                if self.cooked and self.burnt:
                    self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "burnt_steak.png", (256, 256))
                    self.food_name = "burnt_steak"


        if self.food_type == "carrot":
            if self.chop_number == 0:
                self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "carrot.png", (256, 256))
                self.food_name = "unchopped_carrot"
            if self.chop_number == 1:
                self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "carrot_one_chop.png", (256, 256))
                self.food_name = "chopped_carrot_1"
            if self.chop_number == 2:
                self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "carrot_two_chop.png", (256, 256))
                self.food_name = "chopped_carrot_2"
            if self.chop_number == 3:
                self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "carrot_three_chop.png", (256, 256))
                self.food_name = "chopped_carrot_3"

        if self.food_type == "lettuce":
            if self.chop_number == 0:
                self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "lettuce.png", (256, 256))
                self.food_name = "unchopped_lettuce"
            if self.chop_number == 1:
                self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "lettuce_one_chop.png", (256, 256))
                self.food_name = "chopped_lettuce_1"
            if self.chop_number == 2:
                self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "lettuce_two_chop.png", (260, 256))
                self.food_name = "chopped_lettuce_2"
            if self.chop_number == 3:
                self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "lettuce_three_chop.png", (256, 256))
                self.food_name = "chopped_lettuce_3"

        if self.food_type == "salt":
            self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "salt.png", (18 * 5, 39 * 5))
            self.food_name = "salt"



    def combination(self):
        if self.food_name == "whole_steak_with_carrots":
            self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "whole_steak_with_carrots.png", (256, 256))
        if self.food_name == "whole_cooked_steak":
            self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "whole_cooked_steak.png", (256, 256))
        if self.food_name == "whole_steak_with_lettuce":
            self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "whole_steak_with_lettuce.png",(256, 256))
        if self.food_name == "plate_with_steak":
            self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "whole_cooked_steak_with_plate.png",(256, 256))

        if self.food_name == "lettuce_bowl":
            self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "lettuce_bowl.png", (256, 256))
        if self.food_name == "caesar_salad_no_salt":
            self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "caesar_salad_no_salt.png", (256, 256))
        if self.food_name == "caesar_salad":
            self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "caesar_salad.png", (256, 256))


    def chop_food(self):
        self.chop_number = self.chop_number + 1
        if self.chop_number > 3:
            self.chop_number = 3

    def move_food(self, new_pos):
        self.x = new_pos[0]
        self.y = new_pos[1]


