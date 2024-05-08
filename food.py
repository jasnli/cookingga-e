import pygame

def set_photo_and_resize(photo, size):
    image = pygame.image.load(photo)
    image = pygame.transform.scale(image, size)
    return image


class Food:
    def __init__(self, food_type, x, y):
        self.food_type = food_type
        self.cooked = False
        self.x = x
        self.y = y

        if food_type == "steak":
            self.chopped = False
            self.cooking_stage = 0
            if not self.cooked:
                self.image = set_photo_and_resize("raw_steak.png", (256, 256))
                self.image_size = self.image.get_size()
                self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


    def update_photo(self):
        if self.food_type == "steak":
            if self.cooked and not self.chopped:
                self.image = set_photo_and_resize("cooked_steak.png", (256, 256))
                self.image_size = self.image.get_size()
                self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
