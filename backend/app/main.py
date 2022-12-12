"""backend/main.py."""

from dungeon_generator import MazeGenerator
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

# Initialize FastAPI app
app = FastAPI(title='DungeonMazeGenerator',
              description='Generate a maze with a start, treasure and an end point.'
                          'Legend: "x"= starting point, "+": treasure point, "o": end point')


# Endpoint that serves generation of a maze prediction
@app.post("/generate_maze", status_code=200, tags=["Generate maze"])
async def generate_maze(maze_size: int = 4, maze_name: str = None):
    """Generate a maze.

    :param maze_size: int maze size -> to create a 2D grid
    :param maze_name: str, path/name to store the generated maze
    :return: StreamingResponse to plot the maze as a response
    """
    maze_generator = MazeGenerator(maze_size, maze_name)
    buffer = maze_generator.generate()
    buffer.seek(0)  # Return cursor to starting point
    return StreamingResponse(buffer, media_type="image/png")
