from queue import Queue

from .level import Level


class Solver:
    def __init__(self) -> None:
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    def solve(self, level: Level) -> list[tuple[int, int]]:
        level = level.copy()
        path_directions = []
        visited = set()
        queue = Queue()
        queue.put((level, path_directions))

        while not queue.empty():
            current_level, current_path = queue.get()
            visited.add(str(current_level.grid))

            if current_level.solved():
                return current_path

            for direction in self.directions:
                new_level = current_level.copy()
                new_path = current_path.copy()
                new_path.append(direction)

                new_level.move_worker(*direction)

                if str(new_level.grid) not in visited:
                    queue.put((new_level, new_path))

        return []