# DungeonMapGenerator

The objective of this project is to develop a map generator capable of producing a maze with a starting point, an ending
point, and a treasure location. the starting point and the ending point, as well as the treasure point and the
starting point, should be connected by a path.

The map generator creates a QTable through the application of Q-learning, which must subsequently be utilized to create
a path connecting the three randomly generated locations (the starting, ending, and treasure point).

[DungeonMapGenerator](src/README.md) doc

The Maze Generator API Service is built with FastAPI.

FastAPI is a cutting-edge, quick web framework for creating APIs.

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

---

## Run with docker

### Build the image

```bash
docker build -t maze_generator_image .
```

### Run a container

[//]: # (If you want to specify a port mapping: <host_port>:<container_port>)

```bash
docker run -d -e PORT=8080 -p 8092:8080 maze_generator_image
```

or

```bash
docker run -p 8080:8080 maze_generator_image
```

----

## API documentation (provided by Swagger UI)

Access: http://0.0.0.0:8000/docs or http://0.0.0.0:8092/docs if you run the server providing the port 8092 for example.

And you can use `curl` command to query the API and save the image:

```bash
curl -X 'POST' \
  'http://0.0.0.0:8092/generate_maze' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "maze_size": 4,
  "alpha": 0.8,
  "discount": 0.9,
  "epsilon": 0.2,
  "num_episodes": 100000
}' \
  > output.png
```
or
```bash
curl -X 'POST' \
  'http://0.0.0.0:8092/generate_maze' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"maze_size": 4}' \
  > output.png
```

----
#### Generated maze examples:
![](images/example_maze_1.png)
![](images/example_maze_2.png)
---

#### Evaluating the difficulty of a maze:

We can evaluate the difficulty of a maze using the following metrics:

- Completion time of a maze
- The number of Forks along the correct path:
    - If the perfect path only has one branch, then you only need to be lucky once.
- The number of Loops:
  - Path loops can make a maze more difficult because it is simple to realize that you are on the
    wrong road when you reach a dead end, but if you go in circles, you may visit the same path repeatedly before
    realizing you should be somewhere else.
- The number of three-way intersections and number of four-way intersections.
- The number of elbow cells  (e.g. passage entering from downside (going upwards), then turning either right or left)
