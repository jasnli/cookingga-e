import pygame


def set_photo_and_resize(photo, size):
    image = pygame.image.load(photo)
    image = pygame.transform.scale(image, size)
    return image


class Button:
    def __init__(self, button_photo, x, y):
        self.x = x
        self.y = y
        self.image = set_photo_and_resize(button_photo, (57 * 3, 23 * 3))
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

