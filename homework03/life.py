import pathlib
import random
import copy
from typing import List, Optional, Tuple


Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: Tuple[int, int],
        randomize: bool = True,
        max_generations: Optional[float] = float('inf'),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        clist = [[0 for w in range(self.cols)] for h in range(self.rows)]
        if randomize:
            for w in range(self.rows):
                for h in range(self.cols):
                    clist[w][h] = random.randint(0, 1)
        return clist

    def get_neighbours(self, cell: Cell) -> Cells:
        neighbours = []
        row, col = cell
        for w in [-1, 0, 1]:
            for h in [-1, 0, 1]:
                if 0 <= row + w < self.rows and 0 <= col + h < self.cols and (w, h) != (0, 0):
                    neighbours.append(self.curr_generation[row + w][col + h])
        return neighbours


    def get_next_generation(self) -> Grid:
        next_gen = self.create_grid(False)
        for x in range(self.rows):
            for y in range(self.cols):
                new_neighbours = self.get_neighbours((x, y)).count(1)
                if (self.curr_generation[x][y] == 0) and (new_neighbours == 3):
                    next_gen[x][y] = 1
                elif (self.curr_generation[x][y] == 1) and (new_neighbours in [2, 3]):
                    next_gen[x][y] = 1

        return next_gen

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = self.curr_generation
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        return self.generations == self.max_generations

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        return self.curr_generation != self.prev_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        file = open(filename, "r")
        file_grid = [[int(w) for col in zet.strip()] for zet in file]
        file.close()

        game = GameOfLife((len(file_grid), len(file_grid[0])))
        game.curr_generation = file_grid
        return game

    def save(filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename) as file:
            for row in self.curr_generation:
                file.write("".join([str(w) for w in row]))
                file.write("\n")