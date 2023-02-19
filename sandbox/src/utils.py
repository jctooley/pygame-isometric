import os
import pygame


def import_folder(path: str):
    surface_list = []

    asset_path = os.path.join(os.getcwd(), path)

    for _, __, image_files in os.walk(asset_path):
        for image in image_files:
            full_path = os.path.join(asset_path, image)
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list
