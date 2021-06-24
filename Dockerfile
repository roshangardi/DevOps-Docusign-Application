# Use the Python3.7.2 image
FROM python:3.7.2-stretch

# Set the working directory to /app
#WORKDIR /app

# Copy the current directory contents into the container at /app
#ADD app /app
ADD . /app
WORKDIR /app

# Install the dependencies
RUN pip install -r requirements.txt
CMD ["tree"]
#WORKDIR /

# run the command to start uWSGI
EXPOSE 5000:5000
CMD ["python", "run.py"]