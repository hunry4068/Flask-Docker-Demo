# this is an official Python runtime, used as the parent image
FROM python:3.10.5-slim

# adds metadata to an image
LABEL MAINTAINER="Eric Huang"
LABEL GitHub="https://github.com/hunry4068/Flask-Docker-Demo"
LABEL version="0.2"
LABEL description="A Docker container to serve a simple Python Flask APP"

# set the working directory in the container to /app
WORKDIR /app

# add the current directory to the container as /app
ADD . /app

# execute everyone's favorite pip command, pip install -r
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# unblock port 80 for the Flask app to run on
EXPOSE 80

# execute the Flask app
CMD ["python", "app.py"]`