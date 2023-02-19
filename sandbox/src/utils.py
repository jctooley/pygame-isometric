import os
import pygame
from typing import Callable


def import_folder(path: str):
    surface_list = []

    asset_path = os.path.join(os.getcwd(), path)

    for _, __, image_files in os.walk(asset_path):
        for image in image_files:
            full_path = os.path.join(asset_path, image)
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list


class Timer:
    def __init__(self, duration: int, cb: Callable = None):
        self.duration = duration
        self.cb = cb
        self.start_time = 0
        self.active = False

    def activate(self):
        self.active = True
        self.start_time = pygame.time.get_ticks()

    def deactivate(self):
        self.active = False
        self.start_time = 0

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time >= self.duration:
            self.deactivate()
            if self.cb:
                self.cb()
