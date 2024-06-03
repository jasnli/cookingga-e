import pygame


def set_photo_and_resize(photo, size):
    image = pygame.image.load(photo)
    image = pygame.transform.scale(image, size)
    return image


class Appliance:
    def __init__(self, appliance_type, x, y):
        self.x = x
        self.y = y
        self.stove_on = False
        self.stove_animation_pic = 3
        self.appliance = appliance_type

        if self.appliance == "frying_pan":
            self.image = set_photo_and_resize("frying_pan.png", (23 * 10, 42 * 10))
            self.image_size = self.image.get_size()
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

        if self.appliance == "stove":
            if not self.stove_on:
                self.image = set_photo_and_resize("stove_off.png", (64 * 5, 54 * 5))
            self.image_size = self.image.get_size()
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def update_pos(self):
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def update_photo(self, photo):
        if self.appliance == "stove":
            self.image = set_photo_and_resize(photo, (64 * 5, 54 * 5))
            self.image_size = self.image.get_size()
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])