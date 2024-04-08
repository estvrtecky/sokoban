import pygame

from .models import Grid


class Game:
    def __init__(self):
        # Pygame initialization
        pygame.init()
        pygame.font.init()

        self.running = True
        self.grid = Grid()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.grid.move_worker(0, -1)
                if event.key == pygame.K_DOWN:
                    self.grid.move_worker(0, 1)
                if event.key == pygame.K_LEFT:
                    self.grid.move_worker(-1, 0)
                if event.key == pygame.K_RIGHT:
                    self.grid.move_worker(1, 0)

    def run(self):
        screen = pygame.display.set_mode((800, 600))
        clock = pygame.time.Clock()
        pygame.display.set_caption("Sokoban")

        while self.running:
            self.handle_events()
            self.grid.draw(screen)
            pygame.display.update()

        pygame.quit()