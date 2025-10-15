# Dockerfile for the Flexible Environment

# Use an official lightweight Python runtime as a parent image.
FROM python:3.14-slim

# Set the working directory inside the container to /app.
WORKDIR /app

# Copy the requirements file into the container at /app.
COPY requirements.txt .

# Install the Python dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code from the host to the container at /app.
COPY . .

# Define the command to run the application.
# Gunicorn is a production-ready web server.
# App Engine will set the $PORT environment variable, which gunicorn will use.
# We bind to 0.0.0.0 to accept connections from outside the container.
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]
