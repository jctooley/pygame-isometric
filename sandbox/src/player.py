import os
import pygame
from settings import SCREEN_HEIGHT, SCREEN_WIDTH
from utils import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, pos: pygame.Vector2, group: pygame.sprite.Group) -> None:
        super().__init__(group)

        self.import_assets()
        self.status = "down"
        self.status = "down"
        self.frame_index = 0

        # general setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        # movement
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    def import_assets(self):
        print("Importing player assets")
        self.animations = {
            "up": [],
            "down": [],
            "left": {},
            "right": [],
            "up_idle": [],
            "down_idle": [],
            "left_idle": {},
            "right_idle": [],
            "up_hoe": [],
            "down_hoe": [],
            "left_hoe": {},
            "right_hoe": [],
            "up_axe": [],
            "down_axe": [],
            "left_axe": {},
            "right_axe": [],
            "up_water": [],
            "down_water": [],
            "left_water": {},
            "right_water": [],
        }

        for animation in self.animations.keys():
            full_path = os.path.join("sandbox/graphics/character", animation)
            self.animations[animation] = import_folder(full_path)

        print(self.animations)

    def animate(self, dt: float):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = "up"
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = "down"
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = "left"
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = "right"
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            print("space")

    def move(self, dt: float):
        # Only need to continue if there is actual movement
        if self.direction.magnitude() == 0:
            return

        # normalizing a vector
        self.direction = self.direction.normalize()

        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt: float):
        self.input()
        self.move(dt)
        self.animate(dt)
        self.update_status()
