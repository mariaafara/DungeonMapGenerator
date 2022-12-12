"""This module TODO: fill."""
from typing import Tuple

from constants import END_CELL_VALUE, TREASURE_CELL_VALUE


class Board(object):
    """Our Game environment."""

    def __init__(self, map_size: int, starting_point: Tuple[int, int], treasure_point: Tuple[int, int],
                 ending_point: Tuple[int, int]):
        """Constructor init."""
        self.map_width = map_size
        self.map_height = map_size
        self.starting_point, self.ending_point, self.treasure_point = starting_point, ending_point, treasure_point
        self.cell_values = {}  # Maps cell (x, y) to reward r

        self.init_cell_rewards()
        self.is_treasure_reached = False
        self.is_end_reached = False

    def init_cell_rewards(self):
        """Initialize the grid cell rewards, initially each cell reward is filled with 0."""
        for x in range(self.map_width):
            for y in range(self.map_height):
                self.cell_values[(x, y)] = 0
        self.fill_reward_cells()

    def fill_reward_cells(self):
        """Filee the treasure and end cell in the reward dictionary by their constant defined values."""
        self.cell_values[self.treasure_point[0], self.treasure_point[1]] = TREASURE_CELL_VALUE
        self.cell_values[self.ending_point[0], self.ending_point[1]] = END_CELL_VALUE

    def is_terminal_cell(self, coord: Tuple[int, int]) -> bool:
        """Determine if the specified location is a terminal (an end) state.

        In our case, (reaching end_point after reaching the treasure_point) and (reaching treasure_point after
        reaching the end_point) are the end states.
        """
        return (coord == self.ending_point and self.is_treasure_reached) or (
                coord == self.treasure_point and self.is_end_reached)

    def is_valid_cell(self, coord: Tuple[int, int], action: str) -> bool:
        """Check if the next state after executing an action can still be a valid state.

        A valid state is a state that stays within the boundaries of the grid.
        """
        x_coord, y_coord = self.get_cell_after_action(coord, action)
        return 0 <= x_coord < self.map_width and 0 <= y_coord < self.map_height

    def get_cell_after_action(self, coord: Tuple[int, int], action: str) -> Tuple[int, int]:
        """Get the next cell coord after executing an action.

        action: up (x, y+1), down (x, y-1), left (x-1, y), right (x+1, y)
        """
        x_coord, y_coord = coord
        if action == 'left':
            x_coord -= 1
        elif action == 'right':
            x_coord += 1
        elif action == 'up':
            y_coord += 1
        elif action == 'down':
            y_coord -= 1
        return x_coord, y_coord

    def get_cell_value(self, coord: Tuple[int, int]) -> int:
        """Returns the value of a state( represented by its coord).

        For example, Value(self.treasure_point) is 50 and Value(self.end_point) is 25 and the Value(cellOther) is 0.
        """
        return self.cell_values[coord]

    def get_cells(self):
        """TODO:fill."""
        return self.cell_values.keys()
