import sys
import pygame
from sandbox.src.settings import SCREEN_HEIGHT, SCREEN_WIDTH
from sandbox.src.level import Level


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Sandbox Game")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
