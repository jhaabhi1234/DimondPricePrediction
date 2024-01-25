# Use an official Python runtime as a base image
FROM python:3.11-slim-buster

# Set the working directory to /service
WORKDIR /service

# Copy the current directory contents into the container at /service
COPY . .

# Install required dependencies from requirement.txt
RUN pip install --no-cache-dir -r requirement.txt

# Specify the command to run on container start with below comand
ENTRYPOINT ["python3", "app.py"]
