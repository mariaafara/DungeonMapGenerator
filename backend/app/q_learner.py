"""Module that includes the QLearner class."""
import random
from typing import Dict, List, Tuple

from tqdm import tqdm

from backend.app.board import Board
from backend.app.constants import ACTIONS, ALPHA, DISCOUNT, EPSILON, NUM_EPISODES


class QLearner:
    """Implements Q learning algorithm."""

    def __init__(self, map_size, starting_point, treasure_point, ending_point):
        """Constructor init."""
        self.q_table = {}  # Maps cell to possible actions. Actions then map to reward
        self.starting_point, self.ending_point, self.treasure_point = starting_point, ending_point, treasure_point
        self.board = Board(map_size, self.starting_point, self.treasure_point, self.ending_point)
        self.init_q_table()

    def init_q_table(self):
        """Initialize the q_table.

        q_table stores the expected value of a state when an action is taken (e.g. Q(Cell05, ‘down’)).
        It does this for all state and action combinations.

        It is a nested dictionary; The key for the outer dictionary is a state name (e.g. Cell01) that maps
        to a dictionary of valid, possible actions where the action is the key and each action maps to a Q value.
        example: q_table = {cell00 : {‘right’: 0, ‘up’: 0 }, cell01: {‘right’: 0, ‘left’: 0, ‘up’: 0}, …}
        """
        for cell in self.board.get_cells():
            self.q_table[cell] = {}
            for action in ACTIONS:
                if self.board.is_valid_cell(cell, action):
                    self.q_table[cell][action] = 0

    def learn(self):
        """Fills out the q_table.

         The q_table will be updated as the algorithm runs and the agent explores states.

        First we should have inited  q_table(state, action) to 0 for all (state, action) pairs.

        Training algorithm:
        Repeat for episode = 1 ... num of Episodes (epochs)
        Initialize curr_state to start state
        While (curr_state is not TerminalState)
           Choose an action from Actions(curr_state)
           next_state = new state after action a from curr_state
           Q(curr_state, action)= Q(curr_state, action) + α⋅[Value(next_state)+γ⋅maxQ(next_state) − Q(curr_state, action)]
           curr_state = next_state
        """
        for episode in tqdm(range(NUM_EPISODES), desc="Training..."):
            self.curr_state = self.starting_point
            while not self.board.is_terminal_cell(self.curr_state):
                action = self.epsilon_greedy(self.curr_state)  # choose an action
                self.eval_q_function(self.curr_state, action)  # evaluate the optimal value for the current State.
                # go to the next cell which will become the current state
                self.curr_state = self.board.get_cell_after_action(self.curr_state, action)
                if self.curr_state == self.ending_point:  # check if end point is reached and set the boolean to True
                    self.board.is_end_reached = True
                if self.curr_state == self.treasure_point:  # check if treasure point is reached and set the boolean to Tr
                    self.board.is_treasure_reached = True
        print("Finished learning")
        return self.q_table

    def epsilon_greedy(self, state: Tuple[int, int]) -> str:
        """Choose which action to take next (i.e., where to move next).

        Uses Explore and Exploit.
        :param state: coord (x,y) representing a cell
        :return: str: action
        """
        # if a randomly chosen value between 0 and 1 is less than epsilon, choose a random action
        rand_int = random.random()
        # the epsilon represents how often weu want the agent to choose a random action instead of the action with
        # the maximum result.
        if rand_int <= EPSILON:
            # for epsilon % of the time choose from validActions randomly
            return self.explore(state)
        else:  # choose the most promising value from the Q-table for this state.
            return self.exploit(state)

    def explore(self, state: Tuple[int, int]) -> str:
        """Choose a random valid action to go from this state.

        :param state: coord (x,y) representing a cell
        :return: str: action
        """
        valid_actions = list(filter(lambda action: self.board.is_valid_cell(state, action), ACTIONS))
        return random.choice(valid_actions)

    def exploit(self, state: Tuple[int, int]) -> str:
        """Choose the most promising value from the q_table for this state.

        :param state: coord (x,y) representing a cell
        :return: str: action
        """
        # Gets all q_values for specified state for all q values
        q_values = {key: val for key, val in self.q_table.items() if key == state}
        # returns action that yields highest q value
        return max(q_values[state], key=q_values[state].get)

    # Q(s,a)+=α⋅[r+γ⋅maxαQ(s′)−Q(s,a)]
    def eval_q_function(self, coord: Tuple[int, int], action: str):
        """Calculates the optimal value for a given state (coord) and action that leads to a new coord (state).

        The best reward would be Value(new state) plus the maximum value attainable from leaving the new state across all actions
        available from the new state (i.e Actions(next_cell)).
        """
        next_cell = self.board.get_cell_after_action(coord, action)  # Applies action then gets the cell
        next_cell_reward = self.board.get_cell_value(next_cell)  # Get the Reward value of the nextCell.
        # get the optimal value of the next state/Cell
        max_q_next_cell = max(
            [self.q_table[next_cell][action2] for action2 in ACTIONS if self.board.is_valid_cell(next_cell, action2)])

        # Q(s,a)= Q(s, a) + α⋅[Value(s’)+γ⋅maxQ(s′)−Q(s,a)]
        self.q_table[coord][action] += (
                ALPHA * (next_cell_reward + DISCOUNT * max_q_next_cell - self.q_table[coord][action]))

    def get_dir_to_go(self) -> Dict[Tuple[int, int], List[str]]:
        """Get the direction to go from the filled q_table.

        :return: a dictionary: cell as a key, and a list of all its possible actions sorted based on their Q Value.
        """
        dir_to_go = {}
        for k, v in self.q_table.items():
            dir_to_go[k] = sorted(v, key=v.get, reverse=True)
        return dir_to_go
