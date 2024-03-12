# Use an official Python as the base image
FROM python:3.9-bullseye
# Setting the working directory in the container
WORKDIR /app

# Copying the current directory contents into the container at /app
COPY . /app

# Installing any needed dependencies specified
RUN pip install --no-cache-dir flask redis

# Expose port 5000
EXPOSE 5000
# Run app.py when the container launches
# This command tells Docker to run the Python interpreter (python) and pass it the script app.py to execute.
CMD ["python", "app.py"]