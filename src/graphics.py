import pygame

from .config import Config
from .models import BOX, BOX_ON_STORAGE, FLOOR, PLAYER, PLAYER_ON_STORAGE, STORAGE, WALL
from .models import Level


class Graphics:
    def __init__(self) -> None:
        self.config = Config("config.ini")
        self.characters = [BOX, BOX_ON_STORAGE, FLOOR, PLAYER, PLAYER_ON_STORAGE, STORAGE, WALL]
        self.sprites_path = self.config.get("paths", "sprites_path")
        self.sprites_filenames = self.config.items("sprites")
        self.sprites = self.load_sprites()

    def load_sprites(self) -> dict[str, pygame.Surface]:
        """Load the sprites from the sprites folder."""
        sprites = {}
        for charIndex, char in enumerate(self.characters):
            _, filename = self.sprites_filenames[charIndex]
            sprites[char] = pygame.image.load(f"{self.sprites_path}/{filename}")

        return sprites

    def draw(self, screen: pygame.Surface, level: Level) -> None:
        """Draw the level on the screen."""
        screen_width, screen_height = screen.get_size()
        level_width, level_height = level.size()
        cell_size = min(screen_width // level_width, screen_height // level_height)

        for y, row in enumerate(level.grid):
            for x, char in enumerate(row):
                sprite = pygame.transform.scale(self.sprites[char], (cell_size, cell_size))
                screen.blit(sprite, (x * cell_size, y * cell_size))