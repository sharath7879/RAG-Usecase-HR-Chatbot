# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Expose port 5000 to the outside world
EXPOSE 5000

# Define a volume named "app_data" and mount it to /app/download inside the container
VOLUME ["/downloads"]

# Command to run the Flask application
#CMD ["flask", "run", "--host=0.0.0.0"]
ENTRYPOINT [ "python3" ]
CMD [ "fapp.py"]
