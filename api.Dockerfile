# Pull the offical docker image: Base image
FROM python:3.8

ENV PORT=8092
EXPOSE 8080

# Set the work Directory to /app in the container
WORKDIR /app

# ADD and install API requirements
ADD api_requirements.txt /app
RUN pip install -r api_requirements.txt

# ADD and install maze_generator package
ADD src /maze_generator
RUN pip install /maze_generator

ADD serving/api_main.py /app

# Run the web service on container startup. Here we use the uvicorn
# webserver, with one worker process
CMD uvicorn api_main:app --host 0.0.0.0 --port $PORT --workers 1
