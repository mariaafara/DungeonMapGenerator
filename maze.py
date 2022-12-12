"""TODO: fill."""
import io
from typing import List, Tuple

from matplotlib import pyplot as plt


class Cell:
    """A cell in the maze.

    A maze "Cell" is a point in the grid which may be surrounded by walls in these directions:
    up, down, left or right.
    """
    # A wall separates a pair of cells in the up-down or left-right directions.
    wall_pairs = {'up': 'down', 'down': 'up', 'right': 'left', 'left': 'right'}

    def __init__(self, coord):
        """Initialize the cell at coord = (x,y). At first, it is surrounded by walls."""
        self.coord = coord
        self.walls = {'up': True, 'down': True, 'right': True, 'left': True}

    def __str__(self):
        """Define a custom string representation of a cell object.

        :return: str: contains the coord of a cell and its walls' dictionary.
        """
        s = f"coord:{self.coord} -- walls:{self.walls}"
        return s

    def knock_down_wall(self, other, wall):
        """Knock down the wall between cells self and other."""
        self.walls[wall] = False
        other.walls[Cell.wall_pairs[wall]] = False


class Maze:
    """A Maze, represented as a grid of cells."""

    def __init__(self, size, starting_point, treasure_point, ending_point):
        """Initialize the maze grid."""
        self.size = size
        self.starting_point = starting_point  # coordinates of the starting point
        self.ending_point = ending_point
        self.treasure_point = treasure_point
        self.maze_map = [[Cell((x, y)) for y in range(self.size)] for x in
                         range(self.size)]  # initialize a maze_map made up of cells of 4 walls.

    def cell_at(self, coord):
        """Return the Cell object at coord (x,y)."""
        return self.maze_map[coord[0]][coord[1]]

    def make_maze(self, actions: List[Tuple[str, Tuple[int, int]]]):
        """Form the maze with paths.

        Make the maze by knocking down the walls of the adjacent cells that opens a path between the starting point
        and the treasure point, and between the starting point and the ending_point.

        :param actions: List of action and cell tuples e.g. [('left', (2, 2)), ('up', (2, 3)), ('left', (1, 3))]
        """
        current_cell = self.cell_at(self.starting_point)
        for (next_action, next_cell) in actions:  # next_action is the direction to take from the current cell
            next_cell = self.cell_at(next_cell)
            current_cell.knock_down_wall(next_cell, next_action)
            current_cell = next_cell

    def plot(self, maze_name: str = None) -> io.BytesIO:
        """Plot the maze using matplotlib.

        :param maze_name: str path with the maze name to store the maze.
        :return: buffer: maze plot stored in an i/o buffer
        """
        fig, ax = plt.subplots()
        w, h = self.size, self.size
        # plot the boarders of the maze
        ax.plot([0, w], [0, 0], "k")
        ax.plot([0, w], [h, h], "k")
        ax.plot([0, 0], [0, h], "k")
        ax.plot([w, w], [0, h], "k")
        # start building the cells wall by wall, starting from the bottom left (Cell00) and upwards
        for i in range(w):
            for j in range(h):
                cell = self.cell_at((i, j))
                # print(str(cell)) # to see the walls of each cell in the maze grid.
                if cell.walls["up"]:
                    ax.plot([i, i + 1], [j + 1, j + 1], "k")
                if cell.walls["right"]:
                    ax.plot([i + 1, i + 1], [j, j + 1], "k")
        # Mark the start, treasure and end cells with matplotlib markers
        ax.plot(self.starting_point[0] + 0.5, self.starting_point[1] + 0.5, "g", marker="x", markersize=12)
        ax.plot(self.treasure_point[0] + 0.5, self.treasure_point[1] + 0.5, "b", marker="+", markersize=12)
        ax.plot(self.ending_point[0] + 0.5, self.ending_point[1] + 0.5, "r", marker="o", markersize=12)
        plt.axis('off')
        if maze_name:  # if maze_name is provided save the plot to the disk
            fig.savefig(maze_name)
        # store the fig in an i/o buffer and return the buffer
        buffer = io.BytesIO()
        fig.savefig(buffer, format="png")
        return buffer
