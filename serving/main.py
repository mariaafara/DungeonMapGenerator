"""backend/main.py."""

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, StreamingResponse
from maze_generator import MazeGenerator

# Initialize FastAPI app
app = FastAPI(
    title="DungeonMazeGenerator",
    description="Generate a maze with a start, treasure and an end point."
    'Legend: "x"= starting point, "+": treasure point, "o": end point',
)


@app.exception_handler(ValueError)
async def validation_exception_handler(request: Request, exc: ValueError):
    """Return BAD_REQUEST when ValueError is raised."""
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            {"detail": "Maze size should be a strictly positive integer."}
        ),
    )


# Endpoint that serves generation of a maze prediction
@app.post("/generate_maze", status_code=200, tags=["Generate maze"])
async def generate_maze(maze_size: int = 4):
    """Generate a maze.

    :param maze_size: int maze size -> to create a 2D grid
    :return: StreamingResponse to plot the maze as a response
    """
    maze_generator = MazeGenerator(maze_size)
    buffer = maze_generator.generate()
    buffer.seek(0)  # Return cursor to starting point
    return StreamingResponse(buffer, media_type="image/png")
