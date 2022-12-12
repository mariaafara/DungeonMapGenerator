"""Module that contains MazeGenerator."""
import random
from typing import Tuple

from maze import Maze
from q_learner import QLearner


class MazeGenerator:
    """TODO: fill."""

    def __init__(self, map_size):
        """Initializes a MazeGenerator."""
        self.map_size = map_size

        self.starting_point, self.ending_point, self.treasure_point = self.init_points()

        self.maze = Maze(self.map_size, self.starting_point, self.treasure_point, self.ending_point)

        self.q_learner = QLearner(self.map_size, self.starting_point, self.treasure_point, self.ending_point)

        self.is_treasure_reached = False
        self.is_end_reached = False

        self.actions = None

    def __generate_random_point(self, chosen_points: set = None) -> Tuple[int, int]:
        """Generate a random point of (x, y) coordinates."""
        while True:
            point = (random.randint(0, self.map_size - 1), random.randint(0, self.map_size - 1))
            if chosen_points is None or point not in chosen_points:
                return point

    def init_points(self) -> Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]:
        """Initialize starting point, an ending point and a treasure point."""
        starting_point = self.__generate_random_point()
        treasure_point = self.__generate_random_point(chosen_points={starting_point})
        ending_point = self.__generate_random_point(chosen_points={starting_point, treasure_point})
        return starting_point, treasure_point, ending_point

    def is_path_complete(self, coord):
        """Check if there is a complete path formed.

        A complete path exists only if an ending point is reached such that a treasure point has been reached through
        the way, or the other way around.
        """
        return (coord == self.ending_point and self.is_treasure_reached) or (
                coord == self.treasure_point and self.is_end_reached)

    def is_visited_cell(self, coord, visited_cells) -> bool:
        """Check if the specified cell (coord) has been visited before (stored in visted_cells list)."""
        return coord in visited_cells

    def select_actions(self, dir_to_go) -> None:
        """Extract a set of actions and their leading cells."""
        actions = []  # cell as key, action to take as value (the wall between the cell and the next cell that the action take will be removed)
        self.curr_cell = self.starting_point
        visited_cells = {(i, j): 0 for i in range(self.map_size) for j in range(self.map_size)}
        while not self.is_path_complete(self.curr_cell):
            possible_next_actions = dir_to_go[self.curr_cell]

            if visited_cells[self.curr_cell] == len(possible_next_actions):
                action = random.choice(possible_next_actions)
                self.curr_cell = self.q_learner.board.get_cell_after_action(self.curr_cell, action)
            else:
                action, visited_cells[self.curr_cell] = possible_next_actions[visited_cells[self.curr_cell]], \
                                                        visited_cells[self.curr_cell] + 1
                self.curr_cell = self.q_learner.board.get_cell_after_action(self.curr_cell, action)
            if self.curr_cell == self.ending_point:
                self.is_end_reached = True
            if self.curr_cell == self.treasure_point:
                self.is_treasure_reached = True
            actions.append((action, self.curr_cell))
        self.actions = actions

    def generate(self):
        """Generate the dungeon maze."""
        self.q_learner.learn()
        dir_to_go = self.q_learner.get_dir_to_go()
        self.select_actions(dir_to_go)
        self.maze.make_maze(self.actions)
