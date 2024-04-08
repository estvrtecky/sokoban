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

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the level on the screen."""
        screen_width, screen_height = screen.get_size()
        level_width, level_height = self.level_size()
        cell_size = min(screen_width // level_width, screen_height // level_height)

        for y, row in enumerate(self.grid):
            for x, char in enumerate(row):
                colors = {
                    BOX: (255, 0, 0),
                    BOX_ON_STORAGE: (0, 255, 0),
                    FLOOR: (0, 0, 0),
                    PLAYER: (255, 0, 255),
                    PLAYER_ON_STORAGE: (255, 0, 255),
                    STORAGE: (0, 0, 255),
                    WALL: (255, 255, 255)
                }

                pygame.draw.rect(screen, colors[char], (x * cell_size, y * cell_size, cell_size, cell_size))

    def level_size(self) -> tuple[int, int]:
        """
        Returns the size of the level.

        (width, height)
        """
        return len(max(self.grid, key=len)), len(self.grid)

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