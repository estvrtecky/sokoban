import pygame

from .worker import Worker


# Constants
BOX = "$"
BOX_ON_STORAGE = "*"
FLOOR = " "
PLAYER = "@"
PLAYER_ON_STORAGE = "+"
STORAGE = "."
WALL = "#"

class Grid:
    def __init__(self) -> None:
        self.grid = []
        self.worker = Worker()
        self.load_level(1)

    def draw(self, screen):
        for rowIndex, row in enumerate(self.grid):
            for colIndex, char in enumerate(row):
                colors = {
                    BOX: (255, 0, 0),
                    BOX_ON_STORAGE: (0, 255, 0),
                    FLOOR: (0, 0, 0),
                    PLAYER: (255, 0, 255),
                    PLAYER_ON_STORAGE: (255, 0, 255),
                    STORAGE: (0, 0, 255),
                    WALL: (255, 255, 255)
                }

                pygame.draw.rect(
                    screen,
                    colors[char],
                    (colIndex * 10, rowIndex * 10, 10, 10)
                )

    def load_level(self, level: int) -> None:
        """Load a level from a file."""
        with open(f"data/levels/level_{level}.txt", "r") as f:
            self.grid = [list(row.strip()) for row in f.readlines()]

    def move_worker(self, x, y):
        new_x = self.worker.x + x
        new_y = self.worker.y + y

        if self.grid[new_y][new_x] == " ":
            self.grid[self.worker.y][self.worker.x] = " "
            self.grid[new_y][new_x] = "@"

            self.worker.x = new_x
            self.worker.y = new_y

        elif self.grid[new_y][new_x] == "$":
            box_x = new_x + x
            box_y = new_y + y

            if self.grid[box_y][box_x] == " ":
                self.grid[self.worker.y][self.worker.x] = " "
                self.grid[new_y][new_x] = "@"
                self.grid[box_y][box_x] = "$"

                self.worker.x = new_x
                self.worker.y = new_y
