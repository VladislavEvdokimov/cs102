import pygame
from pygame.locals import *

from life import GameOfLife
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        grid = self.cell_size - 1
        for x in range(self.life.rows):
            for y in range(self.life.cols):
                if self.life.curr_generation[y][x] != 0:
                    pygame.draw.rect(
                        self.screen,
                        pygame.Color("green"),
                        (
                            (self.cell_size * x + 1),
                            (self.cell_size * y + 1),
                            grid,
                            grid,
                        ),
                    )
                else:
                    pygame.draw.rect(
                        self.screen,
                        pygame.Color("white"),
                        (
                            (self.cell_size * x + 1),
                            (self.cell_size * y + 1),
                            grid,
                            grid,
                        ),
                    )


    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        pause = False
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    pause = not pause

            self.draw_lines()

            if pause:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        pause = not pause
                    elif event.type == pygame.MOUSEBUTTONUP:
                        file_ = event.pos
                        row = file_[1] // self.cell_size
                        col = file_[0] // self.cell_size
                        if self.life.curr_generation[row][col]:
                            self.life.curr_generation[row][col] = 0
                        else:
                            self.life.curr_generation[row][col] = 1
                        self.draw_grid()
                        pygame.display.flip()
            else:

                self.life.step()
                self.draw_grid()
                pygame.display.flip()
                clock.tick(self.speed)
        pygame.quit()
