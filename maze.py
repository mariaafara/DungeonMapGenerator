"""TODO: fill."""


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
        """TODO: fill."""
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

    def make_maze(self, actions):
        """Form the maze with paths.

        Make the maze by knocking down the walls of the adjacent cells that opens a path between the starting point
        and the treasure point, and between the starting point and the ending_point.
        """
        current_cell = self.cell_at(self.starting_point)
        for (next_action, next_cell) in actions:  # next_action is the direction to take from the current cell
            next_cell = self.cell_at(next_cell)
            current_cell.knock_down_wall(next_cell, next_action)
            current_cell = next_cell
