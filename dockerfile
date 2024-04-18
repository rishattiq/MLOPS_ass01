# Use the official Python image as a base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install dependencies
RUN pip3 install -r requirements.txt

# Copy the entire current directory into the container at /app
COPY . .

# Expose port 5000 to allow communication to/from server
EXPOSE 5000

# Command to run the Python script
CMD [ "python", "app.py" ]
