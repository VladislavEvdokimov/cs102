import copy
import pathlib
import random
from typing import List, Optional, Tuple

Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: Tuple[int, int],
        randomize: bool = True,
        max_generations: Optional[float] = float("inf"),
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

        grid = []
        if randomize == False:
            grid = [[0 for w in range(self.cols)] for h in range(self.rows)]
        else:
            grid = [[random.randint(0, 1) for w in range(self.cols)] for h in range(self.rows)]
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:

        neighbours = []
        row, col = cell
        for h in range(max(0, row - 1), min(self.rows, row + 2)):
            for w in range(max(0, col - 1), min(self.cols, col + 2)):
                if (h, w) != cell:
                    neighbours.append(self.curr_generation[h][w])
        return neighbours

    def get_next_generation(self) -> Grid:

        copy_grid = self.create_grid(False)
        for h in range(self.rows):
            for w in range(self.cols):
                if (self.curr_generation[h][w] == 0) and sum(self.get_neighbours((h, w))) == 3:
                    copy_grid[h][w] = 1
                elif (self.curr_generation[h][w] == 1) and (
                    1 < sum(self.get_neighbours((h, w))) < 4
                ):
                    copy_grid[h][w] = 1

        return copy_grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """

        self.prev_generation = copy.deepcopy(self.curr_generation)
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        if self.generations == self.max_generations:
            return True
        else:
            return False

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """

        if self.prev_generation != self.curr_generation:
            return True
        else:
            return False

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """

        doc = open(filename, "r")
        doc_grid = [[int(col) for col in row.strip()] for row in doc]
        doc.close()

        game = GameOfLife((len(doc_grid), len(doc_grid[0])))
        game.curr_generation = doc_grid
        return game

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """

        doc = open(filename, "w")
        for row in self.curr_generation:
            for col in row:
                doc.write(str(col))
            doc.write("\n")
        doc.close()
