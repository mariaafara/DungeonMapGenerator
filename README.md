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

```
docker build -t maze_generator_image .
```

### Run a container

[//]: # (If you want to specify a port mapping: <host_port>:<container_port>)
```
docker run -d -e PORT=8080 -p 8092:8080 maze_generator_image
```

or

```
docker run -p 8080:8080 maze_generator_image
```

----

## API documentation (provided by Swagger UI)

Access: http://0.0.0.0:8000/docs or http://0.0.0.0:8092/docs if you run the server providing the port 8092 for example.

And you can use `curl` command to query the API and save the image:
```bash
curl -X 'POST' \
  'http://localhost:8092/generate_maze?maze_size=4' \
  -H 'accept: application/json' \
  > output.png
```
