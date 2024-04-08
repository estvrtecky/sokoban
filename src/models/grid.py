import pygame


class Grid:
    def __init__(self) -> None:
        self.grid = [
            ["#"] * 5,
            ["#", " ", " ", " ", "#"],
            ["#", " ", "W", " ", "#"],
            ["#", " ", " ", " ", "#"],
            ["#"] * 5
        ]

    def draw(self, screen):
        for rowIndex, row in enumerate(self.grid):
            for colIndex, char in enumerate(row):
                if char == "#":
                    color = (255, 255, 255)
                elif char == " ":
                    color = (0, 0, 0)
                elif char == "W":
                    color = (255, 0, 0)

                pygame.draw.rect(
                    screen,
                    color,
                    (colIndex * 10, rowIndex * 10, 10, 10)
                )