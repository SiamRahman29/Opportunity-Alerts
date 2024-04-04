# Use an official Python runtime as a parent image
FROM python:3.11.8-bookworm

# The environment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# Creating root directory for our project in the container
RUN mkdir -p /comps

# Setting the working directory to /comps
WORKDIR /comps

# Copying the current directory contents into the container at /comps
COPY . /comps/

# Installing needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Binding a port
EXPOSE 8000

# Command to run the app
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
