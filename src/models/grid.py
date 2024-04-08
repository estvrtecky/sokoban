import pygame

from .worker import Worker


class Grid:
    def __init__(self) -> None:
        self.grid = [
            ["#"] * 5,
            ["#", "W", " ", " ", "#"],
            ["#", " ", "B", " ", "#"],
            ["#", " ", " ", " ", "#"],
            ["#"] * 5
        ]

        self.worker = Worker()

    def draw(self, screen):
        for rowIndex, row in enumerate(self.grid):
            for colIndex, char in enumerate(row):
                if char == "#":
                    color = (255, 255, 255)
                elif char == " ":
                    color = (0, 0, 0)
                elif char == "W":
                    color = (255, 0, 0)
                elif char == "B":
                    color = (0, 0, 255)

                pygame.draw.rect(
                    screen,
                    color,
                    (colIndex * 10, rowIndex * 10, 10, 10)
                )

    def move_worker(self, x, y):
        new_x = self.worker.x + x
        new_y = self.worker.y + y

        if self.grid[new_y][new_x] == " ":
            self.grid[self.worker.y][self.worker.x] = " "
            self.grid[new_y][new_x] = "W"

            self.worker.x = new_x
            self.worker.y = new_y

        elif self.grid[new_y][new_x] == "B":
            box_x = new_x + x
            box_y = new_y + y

            if self.grid[box_y][box_x] == " ":
                self.grid[self.worker.y][self.worker.x] = " "
                self.grid[new_y][new_x] = "W"
                self.grid[box_y][box_x] = "B"

                self.worker.x = new_x
                self.worker.y = new_y
