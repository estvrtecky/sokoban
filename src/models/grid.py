import pygame


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

    def find_player(self) -> tuple[int, int]:
        """Find the player's position in the level."""
        for y, row in enumerate(self.grid):
            for x, char in enumerate(row):
                if char in (PLAYER, PLAYER_ON_STORAGE):
                    return x, y

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

    def move_worker(self, x: int, y: int) -> None:
        """Move the player in the grid."""
        player_x, player_y = self.find_player()
        current = self.grid[player_y][player_x]
        adjacent = self.grid[player_y + y][player_x + x]
        try:
            two_steps_ahead = self.grid[player_y + y * 2][player_x + x * 2]
        except IndexError:
            return

        if current == PLAYER:
            if adjacent == FLOOR:
                self.grid[player_y][player_x] = FLOOR
                self.grid[player_y + y][player_x + x] = PLAYER
            elif adjacent == STORAGE:
                self.grid[player_y][player_x] = FLOOR
                self.grid[player_y + y][player_x + x] = PLAYER_ON_STORAGE
            elif adjacent == BOX:
                if two_steps_ahead == FLOOR:
                    self.grid[player_y][player_x] = FLOOR
                    self.grid[player_y + y][player_x + x] = PLAYER
                    self.grid[player_y + y * 2][player_x + x * 2] = BOX
                elif two_steps_ahead == STORAGE:
                    self.grid[player_y][player_x] = FLOOR
                    self.grid[player_y + y][player_x + x] = PLAYER
                    self.grid[player_y + y * 2][player_x + x * 2] = BOX_ON_STORAGE
            elif adjacent == BOX_ON_STORAGE:
                if two_steps_ahead == FLOOR:
                    self.grid[player_y][player_x] = FLOOR
                    self.grid[player_y + y][player_x + x] = PLAYER_ON_STORAGE
                    self.grid[player_y + y * 2][player_x + x * 2] = BOX
                elif two_steps_ahead == STORAGE:
                    self.grid[player_y][player_x] = FLOOR
                    self.grid[player_y + y][player_x + x] = PLAYER_ON_STORAGE
                    self.grid[player_y + y * 2][player_x + x * 2] = BOX_ON_STORAGE

        elif current == PLAYER_ON_STORAGE:
            if adjacent == FLOOR:
                self.grid[player_y][player_x] = STORAGE
                self.grid[player_y + y][player_x + x] = PLAYER
            elif adjacent == STORAGE:
                self.grid[player_y][player_x] = STORAGE
                self.grid[player_y + y][player_x + x] = PLAYER_ON_STORAGE
            elif adjacent == BOX:
                if two_steps_ahead == FLOOR:
                    self.grid[player_y][player_x] = STORAGE
                    self.grid[player_y + y][player_x + x] = PLAYER
                    self.grid[player_y + y * 2][player_x + x * 2] = BOX
                elif two_steps_ahead == STORAGE:
                    self.grid[player_y][player_x] = STORAGE
                    self.grid[player_y + y][player_x + x] = PLAYER
                    self.grid[player_y + y * 2][player_x + x * 2] = BOX_ON_STORAGE
            elif adjacent == BOX_ON_STORAGE:
                if two_steps_ahead == FLOOR:
                    self.grid[player_y][player_x] = STORAGE
                    self.grid[player_y + y][player_x + x] = PLAYER_ON_STORAGE
                    self.grid[player_y + y * 2][player_x + x * 2] = BOX
                elif two_steps_ahead == STORAGE:
                    self.grid[player_y][player_x] = STORAGE
                    self.grid[player_y + y][player_x + x] = PLAYER_ON_STORAGE
                    self.grid[player_y + y * 2][player_x + x * 2] = BOX_ON_STORAGE