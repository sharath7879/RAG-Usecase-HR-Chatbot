# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory inside the container
WORKDIR /chroma

# Copy the requirements file into the container at /app
COPY requirements.txt /chroma/

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /chroma

# Define a volume named "app_data" and mount it to /app/download inside the container
VOLUME ["/chroma/downloads", "/chroma/db_files"]

# Command to run the Flask application

ENTRYPOINT [ "python3" ]
CMD [ "app.py"]
