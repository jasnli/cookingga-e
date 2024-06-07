import pygame


def set_photo_and_resize(photo, size):
    image = pygame.image.load(photo)
    image = pygame.transform.scale(image, size)
    return image


def rect_updater(picture_size, picture, x, y, rectangle, image_picture):
    picture = set_photo_and_resize(image_picture, (256, 256))
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
            self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "carrot.png")
            self.food_name = "unchopped_carrot"

        if food_type == "lettuce":  # LETTUCE
            self.image = set_photo_and_resize("lettuce.png", (256, 256))
            self.image_size = self.image.get_size()
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
            self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "lettuce.png")
            self.food_name = "unchopped_lettuce"

        # TEMPORARY
        if food_type == "whole_cooked_steak":
            self.image = set_photo_and_resize("whole_cooked_steak.png", (256, 256))
            self.image_size = self.image.get_size()
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
            self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "whole_cooked_steak.png")
            self.food_name = "whole_cooked_steak"


    def update_photo(self):
        if self.food_type == "steak":
            if not self.cooked:
                if self.chop_number == 0:
                    self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "raw_steak.png")
                    self.food_name = "raw_steak"
                if self.chop_number == 1:
                    self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "raw_steak_cut_1.png")
                    self.food_name = "raw_steak_cut1"
                if self.chop_number == 2:
                    self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "raw_steak_cut_2.png")
                    self.food_name = "raw_steak_cut2"
                if self.chop_number == 3:
                    self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "raw_steak_cut_3.png")
                    self.food_name = "raw_steak_cut3"
            if self.cooked and not self.burnt:
                if self.chop_number == 0:
                    self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "cooked_steak.png")
                    self.food_name = "cooked_steak_uncut"
                if self.chop_number == 1:
                    self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "cooked_steak_cut_1.png")
                    self.food_name = "cooked_steak_cut1"
                if self.chop_number == 2:
                    self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "cooked_steak_cut_2.png")
                    self.food_name = "cooked_steak_cut2"
                if self.chop_number == 3:
                    self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "cooked_steak_cut_3.png")
                    self.food_name = "cooked_steak_cut3"
            if self.cooked and self.burnt:
                if self.chop_number == 0:
                    self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "burnt_steak.png")
                    self.food_name = "burnt_steak"
                if self.chop_number == 1:
                    self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "burnt_steak_cut_1.png")
                    self.food_name = "burnt_steak_1"
                if self.chop_number == 2:
                    self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "burnt_steak_cut_2.png")
                    self.food_name = "burnt_steak_2"
                if self.chop_number == 3:
                    self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "burnt_steak_cut_3.png")
                    self.food_name = "burnt_steak_3"


        if self.food_type == "carrot":
            if self.chop_number == 0:
                self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "carrot.png")
                self.food_name = "unchopped_carrot"
            if self.chop_number == 1:
                self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "carrot_one_chop.png")
                self.food_name = "chopped_carrot_1"
            if self.chop_number == 2:
                self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "carrot_two_chop.png")
                self.food_name = "chopped_carrot_2"
            if self.chop_number == 3:
                self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "carrot_three_chop.png")
                self.food_name = "chopped_carrot_3"

        if self.food_type == "lettuce":
            if self.chop_number == 0:
                self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "lettuce.png")
                self.food_name = "unchopped_lettuce"
            if self.chop_number == 1:
                self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "lettuce_one_chop.png")
                self.food_name = "chopped_lettuce_1"
            if self.chop_number == 2:
                self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "lettuce_two_chop.png")
                self.food_name = "chopped_lettuce_2"
            if self.chop_number == 3:
                self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "lettuce_three_chop.png")
                self.food_name = "chopped_lettuce_3"

        if self.food_name == "whole_cooked_steak":
            self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "whole_cooked_steak.png")
        if self.food_name == "cut_steak_meal_cooked":
            self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "cut_steak_meal_cooked.png")

    def chop_food(self):
        self.chop_number = self.chop_number + 1
        if self.chop_number > 3:
            self.chop_number = 3

    def move_food(self, new_pos):
        self.x = new_pos[0]
        self.y = new_pos[1]


