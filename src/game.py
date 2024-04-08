import pygame

from .models import Grid


class Game:
    def __init__(self):
        # Pygame initialization
        pygame.init()
        pygame.font.init()

        self.running = True
        self.grid = Grid()
        self.levels = 2
        self.current_level = 1

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                # Movement
                if event.key == pygame.K_UP:
                    self.grid.move_worker(0, -1)
                if event.key == pygame.K_DOWN:
                    self.grid.move_worker(0, 1)
                if event.key == pygame.K_LEFT:
                    self.grid.move_worker(-1, 0)
                if event.key == pygame.K_RIGHT:
                    self.grid.move_worker(1, 0)
                # Restart
                if event.key == pygame.K_r:
                    self.grid.load_level(self.current_level)

    def run(self):
        screen = pygame.display.set_mode((800, 600))
        clock = pygame.time.Clock()
        pygame.display.set_caption("Sokoban")
        self.grid.load_level(self.current_level)

        while self.running:
            self.handle_events()

            self.grid.draw(screen)
            if self.grid.level_solved() and self.current_level < self.levels:
                    self.current_level += 1
                    self.grid.load_level(self.current_level)

            pygame.display.update()

        pygame.quit()