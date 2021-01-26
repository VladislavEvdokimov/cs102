import curses
import curses.ascii
import pathlib
from time import sleep

from life import GameOfLife
from ui import UI


class Console(UI):

    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)
        self.save_path = save_path

    def draw_borders(self, screen) -> None:
        """ Отобразить рамку. """
        screen.clear()

    def draw_grid(self, screen) -> None:
        """ Отобразить состояние клеток. """
        for w in range(self.life.rows):
            for h in range(self.life.cols):
                if self.life.curr_generation[w][h] == 1:
                    screen.addch(w + 1, h + 1, "*")
                else:
                    screen.addch(w + 1, h + 1, " ")

    def run(self) -> None:
        screen = curses.initscr()
        screen = curses.initscr()
        sc = screen.derwin(self.rows, self.cols, 0, 0)
        self.draw_borders(sc)

        try:
            while self.life.is_changing or not self.life.is_max_generations_exceeded:
                self.draw_borders(sc)
                self.draw_grid(sc)
                sc.refresh()
                self.life.step()
                curses.endwin()


def main():
    game = GameOfLife(size=(32, 80))
    app = Console(game)
    app.run()
        
if __name__ == "__main__":
    life = GameOfLife((15, 30), randomize=True)
    ui = Console(life, save_path=pathlib.Path("fileui.txt"))
    ui.run()


