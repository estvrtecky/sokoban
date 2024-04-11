import pygame

from .config import Config
from .models import Level


class Game:
    def __init__(self):
        # Pygame initialization
        pygame.init()
        pygame.font.init()

        # Game objects
        self.level = Level()
        self.config = Config("config.ini")

        self.levels_path = self.config.get("paths", "levels_path")
        self.running = True
        self.levels = 2
        self.current_level = 1

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                # Movement
                if event.key == pygame.K_UP:
                    self.level.move_worker(0, -1)
                if event.key == pygame.K_DOWN:
                    self.level.move_worker(0, 1)
                if event.key == pygame.K_LEFT:
                    self.level.move_worker(-1, 0)
                if event.key == pygame.K_RIGHT:
                    self.level.move_worker(1, 0)
                # Restart
                if event.key == pygame.K_r:
                    self.level.load(self.levels_path, self.current_level)

    def run(self):
        screen = pygame.display.set_mode((800, 600))
        clock = pygame.time.Clock()
        pygame.display.set_caption("Sokoban")
        self.level.load(self.levels_path, self.current_level)

        while self.running:
            self.handle_events()

            self.level.draw(screen)
            if self.level.solved() and self.current_level < self.levels:
                self.current_level += 1
                self.level.load(self.levels_path, self.current_level)

            pygame.display.update()

        pygame.quit()