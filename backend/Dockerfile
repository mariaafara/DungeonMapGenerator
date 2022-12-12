# Pull the offical docker image: Base image
FROM python:3.8

# Set working directory
WORKDIR /app

ADD requirements.txt /app

# Install dependencies
RUN pip install -r requirements.txt

# Copy all the modules to an app folder
ADD app/board.py app/
ADD app/maze.py app/
ADD app/constants.py app/
ADD app/dungeon_generator.py app/
ADD app/main.py app/
ADD app/q_learner.py app/

ADD __init__.py /app
ADD app/main.py /app

ENV PYTHONPATH "${PYTHONPATH}:/app/app"

# Run the application
ENV PORT=8080
EXPOSE 8080
CMD uvicorn main:app --host 0.0.0.0 --port $PORT --workers 1
