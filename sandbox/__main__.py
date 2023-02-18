from typing import List
import os
import datetime
import pygame


def main():
    print("Sandbox")
    dt = datetime.datetime.today()
    print(f"Today is {dt}")

    my_list: List = []
    my_list.append({"hello": "world"})
    print(f"My list is {my_list}")

    cwd = os.getcwd()
    print(f"Current working directory is {cwd}")

    vec2 = pygame.Vector2(25, 75)
    vec3 = pygame.Vector3(10, 20, 30)

    vec2.x = 50
    vec2.y = 50

    vec2.t


if __name__ == "__main__":
    main()
