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


class Maze:
    """A Maze, represented as a grid of cells."""

    def __init__(self, size, starting_point, treasure_point, ending_point):
        """Initialize the maze grid."""
        self.size = size
        self.starting_point = starting_point  # coordinates of the starting point
        self.ending_point = ending_point
        self.treasure_point = treasure_point
