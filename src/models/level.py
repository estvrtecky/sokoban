import os

from .characters import BOX, BOX_ON_STORAGE, FLOOR, PLAYER, PLAYER_ON_STORAGE, STORAGE, WALL


class Level:
    def __init__(self) -> None:
        self.grid = []

    def find_player(self) -> tuple[int, int]:
        """Find the player's position in the level."""
        for y, row in enumerate(self.grid):
            for x, char in enumerate(row):
                if char in (PLAYER, PLAYER_ON_STORAGE):
                    return x, y

    def load(self, path: str, level: int) -> None:
        """Load a level from a file."""
        level_path = f"{path}/level_{level}.txt"

        if not os.path.exists(level_path):
            raise FileNotFoundError(f"Level file not found: {level_path}")

        with open(level_path, "r") as f:
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

    def size(self) -> tuple[int, int]:
        """Returns the size of the level. (width, height)"""
        return len(max(self.grid, key=len)), len(self.grid)

    def solved(self) -> bool:
        """Check if the level is solved."""
        return all(BOX not in row for row in self.grid)