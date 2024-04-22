import pygame

from .models import BOX, BOX_ON_STORAGE, FLOOR, PLAYER, PLAYER_ON_STORAGE, STORAGE, WALL
from .models import Level


class Graphics:
    def __init__(self) -> None:
        pass

    def draw(self, screen: pygame.Surface, level: Level) -> None:
        """Draw the level on the screen."""
        screen_width, screen_height = screen.get_size()
        level_width, level_height = level.size()
        cell_size = min(screen_width // level_width, screen_height // level_height)

        colors = {
            BOX: (255, 0, 0),
            BOX_ON_STORAGE: (0, 255, 0),
            FLOOR: (0, 0, 0),
            PLAYER: (255, 0, 255),
            PLAYER_ON_STORAGE: (255, 0, 255),
            STORAGE: (0, 0, 255),
            WALL: (255, 255, 255)
        }

        for y, row in enumerate(level.grid):
            for x, char in enumerate(row):
                pygame.draw.rect(screen, colors[char], (x * cell_size, y * cell_size, cell_size, cell_size))