import pygame

from .models import Grid, Worker


class Game:
    def __init__(self):
        # Pygame initialization
        pygame.init()
        pygame.font.init()

        self.running = True
        self.worker = Worker()
        self.grid = Grid()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.move_worker(0, -1)
                if event.key == pygame.K_DOWN:
                    self.move_worker(0, 1)
                if event.key == pygame.K_LEFT:
                    self.move_worker(-1, 0)
                if event.key == pygame.K_RIGHT:
                    self.move_worker(1, 0)

    def move_worker(self, x, y):
        new_x = self.worker.x + x
        new_y = self.worker.y + y

        if self.grid.grid[new_y][new_x] == " ":
            self.grid.grid[self.worker.y][self.worker.x] = " "
            self.grid.grid[new_y][new_x] = "W"

            self.worker.x = new_x
            self.worker.y = new_y

    def run(self):
        screen = pygame.display.set_mode((800, 600))
        clock = pygame.time.Clock()
        pygame.display.set_caption("Sokoban")

        while self.running:
            self.handle_events()
            self.grid.draw(screen)
            pygame.display.update()

        pygame.quit()