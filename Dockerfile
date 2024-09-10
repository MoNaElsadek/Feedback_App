# Use an official Python runtime as a parent image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file to the working directory
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port that Flask will run on
EXPOSE 8000

# Set the command to run the app
CMD ["python", "app.py"]

