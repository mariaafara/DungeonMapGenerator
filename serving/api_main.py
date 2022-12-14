"""backend/main.py."""
from typing import Optional

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from maze_generator import ALPHA, DISCOUNT, EPSILON, NUM_EPISODES, MazeGenerator
from pydantic import BaseModel, validator

# Initialize FastAPI app
app = FastAPI(
    title="DungeonMazeGenerator",
    description="Generate a maze with a start, treasure and an end point."
    'Legend: "x"= starting point, "+": treasure point, "o": end point',
)


class MazeGeneratorRequest(BaseModel):
    """MazeGeneratorRequest Model."""

    maze_size: int = 4
    alpha: Optional[float] = ALPHA
    discount: Optional[float] = DISCOUNT
    epsilon: Optional[float] = EPSILON
    num_episodes: Optional[int] = NUM_EPISODES

    @validator("num_episodes", pre=True)
    def validate_num_episodes(cls, v):
        if v <= 0:
            raise ValueError("num_episodes should be a positive integer")
        return v

    @validator("epsilon", pre=True)
    def validate_epsilon(cls, v):
        if not (0 <= v <= 1):
            raise ValueError("epsilon should be between 0 and 1")
        return v

    @validator("alpha", pre=True)
    def validate_alpha(cls, v):
        if not (0 <= v <= 1):
            raise ValueError("alpha should be between 0 and 1")
        return v

    @validator("maze_size", pre=True)
    def validate_maze_size(cls, v):
        if v <= 1:
            raise ValueError("maze_size should be at least 2")
        return v

    @validator("discount", pre=True)
    def validate_discount(cls, v):
        if not (0 <= v <= 1):
            raise ValueError("discount should be between 0 and 1")
        return v


# Endpoint that serves generation of a maze prediction
@app.post("/generate_maze", status_code=200, tags=["Generate maze"])
async def generate_maze(maze_generator_request: MazeGeneratorRequest):
    """Generate a maze.

    :param maze_generator_request: MazeGeneratorRequest model
    :return: StreamingResponse to plot the maze as a response
    """
    maze_generator = MazeGenerator(
        maze_size=maze_generator_request.maze_size,
        alpha=maze_generator_request.alpha,
        discount=maze_generator_request.discount,
        epsilon=maze_generator_request.epsilon,
        num_episodes=maze_generator_request.num_episodes,
    )
    buffer = maze_generator.generate()
    buffer.seek(0)  # Return cursor to starting point
    return StreamingResponse(buffer, media_type="image/png")
