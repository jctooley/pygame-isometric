import os
import pygame
from settings import SCREEN_HEIGHT, SCREEN_WIDTH
from utils import import_folder, Timer


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

        # timers
        self.timers = {"tool_use": Timer(350, self.use_tool), "tool_switch": Timer(200)}

        # tools
        self.tools = ["hoe", "axe", "water"]
        self.tool_index = 0
        self.selected_tool = self.tools[self.tool_index]

    def use_tool(self):
        pass

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

        if self.timers["tool_use"].active:
            # No movement allowed when tools are active
            return

        # directions
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

        # tool use
        if keys[pygame.K_SPACE]:
            self.timers["tool_use"].activate()
            self.direction = pygame.math.Vector2()
            self.frame_index = 0

        # change tool
        if keys[pygame.K_t] and not self.timers["tool_switch"].active:
            self.timers["tool_switch"].activate()
            self.change_tool()

    def change_tool(self):
        self.tool_index += 1
        self.tool_index = self.tool_index if self.tool_index < len(self.tools) else 0
        print(self.tool_index)
        self.selected_tool = self.tools[self.tool_index]

        if self.timers["tool_use"].active:
            self.status = self.status.split("_")[0] + "_" + self.selected_tool

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

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def update(self, dt: float):
        self.input()
        self.move(dt)
        self.animate(dt)
        self.update_status()
        self.update_timers()
