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
        self.x = x
        self.y = y
        self.chop_number = 0
        self.movable = True

        if food_type == "steak":
            self.cooking_stage = 0
            if not self.cooked:
                self.image = set_photo_and_resize("raw_steak.png", (256, 256))
                self.image_size = self.image.get_size()
                self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def update_photo(self):
        if self.food_type == "steak":
            if not self.cooked:
                if self.chop_number == 0:
                    self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "raw_steak.png")
                if self.chop_number == 1:
                    self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "raw_steak_cut_1.png")
                if self.chop_number == 2:
                    self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "raw_steak_cut_2.png")
                if self.chop_number == 3:
                    self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "raw_steak_cut_3.png")
            if self.cooked:
                if self.chop_number == 0:
                    self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "cooked_steak.png")
                if self.chop_number == 1:
                    self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "cooked_steak_cut_1.png")
                if self.chop_number == 2:
                    self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "cooked_steak_cut_2.png")
                if self.chop_number == 3:
                    self.rect, self.image_size, self.image = rect_updater(self.image_size, self.image, self.x, self.y, self.rect, "cooked_steak_cut_3.png")

    def chop_food(self):
        self.chop_number = self.chop_number + 1

    def move_food(self, new_pos):
        self.x = new_pos[0]
        self.y = new_pos[1]


