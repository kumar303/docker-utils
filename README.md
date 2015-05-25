A series of utilities for Docker compose. Designed to be used as a wrapper around docker-compose. All the commands of Docker compose are imported and available.

## Install

You will need Python and pip, the same as for installing docker-compose.

    pip install docker-utils

## Usage

To get a list of all available commands. Note that all the docker-compose commands are available.

    docker-utils help

Like docker-compose you will likely want to set the `COMPOSE_FILE` and `COMPOSE_PROJECT_NAME` environment variables.

### Available commands

#### bash

    docker-utils bash [SERVICE]

Run a bash prompt in the container specified in the service. If no SERVICE is specified then it will look for the closest Dockerfile and try to find that container.

This is equivalent (but more friendly than) a combination of docker exec, docker ps, sed and other combinations.

#### lint

    docker-utils lint

Performs a simple lint over the YAML file to try and find some basic errors. This also has the effect of parsing the file through docker-compose without executing any other commands, providing more checks.

#### listen

    docker-utils listen [HOST] [PORT]

Runs a simple HTTP server on the HOST (default localhost) and PORT (default 8000). If Docker Hub sends a webhook to this server it will, check that the image exists in the project and then issue a `docker-compose pull` command on the image.

Press CTRL+C to exit. 
