# DungeonMapGenerator

The objective of this project is to develop a map generator capable of producing a maze with a starting point, an ending
point, and a treasure location. the starting point and the ending point, as well as the treasure point and the
starting point, should be connected by a path.

The map generator creates a QTable through the application of Q-learning, which must subsequently be utilized to create
a path connecting the three randomly generated locations (the starting, ending, and treasure point).

# The approach to generate the maze:

The maze is thought to be made up of a grid of cells, each of which has four walls at first (up, left, right and down).
We will attempt to create a path or paths that visit all the cells that lead to the desired path carving starting from
the randomly created starting cell (point). The process is as follows:

- A collection of actions and their leading cells are derived from the learned Q table. Based on their Q value, the
  optimal actions are chosen in the learned q table so that the cell they lead to should receive the fewest visits.
- The initial cell goes to another and then to another based on the chosen list of activities. A path between the
  starting point and the treasure point and between the starting point and the finishing point is opened by tearing down
  the locked maze walls.

# Reinforcement Learning: Q learning

The environment for this problem is a 2D board.

An agent (the learner and decision maker) is placed somewhere in the maze. This somewhere would be the random generated
starting point. The agents' goal is to learn a path between the starting point and a treasure (located randomly in the
maze) i.e. crave a path to reach the treasure, and to also learn a path to reach the end point (randomly generated as
well) as quickly as possible.

To learn the paths, the agent moves through the maze in a succession of steps. For every step the agent must decide
which action to take. The options are move left, right, up or down.

For this purpose the agent is trained; it learns/fills a QTable which tells what is the best next move to make (Explore
or Exploit). With every step the agent incurs nothing or/and - when finally reaching the end - a reward.

-----

## Run locally

### Install dependencies

```
pip install -r backend/requirements.txt
```

### Run server

```
uvicorn backend.main:app --reload
```

#### With a custom port and workers

```
uvicorn backend.main:app --reload --workers 1 --host 0.0.0.0 --port 8092
```

### API documentation (provided by Swagger UI)

Access: http://0.0.0.0:8000/docs or http://0.0.0.0:8092/docs if you run the server providing the port 8092 for example.
