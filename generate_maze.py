"""Main."""
from src.maze_generator import MazeGenerator

if __name__ == '__main__':
    map_size = 6
    maze_path = "generated_maze.png"
    maze_generator = MazeGenerator(map_size, maze_path)
    b = maze_generator.generate()

    print(f"starting_point: {maze_generator.starting_point},"
          f" treasure_point: {maze_generator.treasure_point}, ending_point: {maze_generator.ending_point}")
    print("Start from cell: ", maze_generator.starting_point,
          " then follow the following actions (action, next cell): ")
    print(maze_generator.actions)
