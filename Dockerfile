# Get Docker Image from hub.docker.com to use as our base
FROM python:3.9.6

# List of environments 
ENV DATABASE_URL=[Change database url here]
ENV FLASK_ENV=development
ENV FLASK_APP=server.py

# Creating which directory we want to be our work directory
WORKDIR /app

# Copy the necessary file to build our pipenv
COPY Pipfile ./
COPY Pipfile.lock ./

# Run these commands to setup 
RUN pip3 install pipenv
RUN pipenv install

# Copy all of our hostfile to the working directory we created
COPY . /app

# Open this port for the host to listen to
EXPOSE 8000

# Final command to run the server (make sure to bind to 0.0.0.0)
CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:8000", "server:app"]