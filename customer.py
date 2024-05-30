import pygame
import random

class Customer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.customer_image = pygame.image.load("customer_1.png")
        self.image_size = self.customer_image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.order = []

        # index 0: 1 cooked steak whole, 2 cooked steak chopped
        # index 1: 1 fruit salad, 2 vegetable salad
        # index 2: 1 soda, 2 orange juice, 3 water, 4 milkshake

    def customer_updater(self, image):
        self.customer_image = pygame.image.load(image)
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def random_order(self):
        main_dish = random.randint(1, 2)
        side_dish = random.randint(1, 2)
        drink = random.randint(1, 4)
        self.order = [main_dish, side_dish, drink]
