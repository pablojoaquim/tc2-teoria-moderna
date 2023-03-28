## GENERETING DOCKER IMAGE
#### CLONE THE REPO , ADD VARIABLES TO env_variables.env , and then run the following Docker commands:

```console
docker build -f Dockerfile -t app:latest .
docker run -p 5000:5000 app
```

## DOCKER COMPOSE
Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services.
Using Compose is basically a three-step process:
- Define your app’s environment with a Dockerfile so it can be reproduced anywhere.
- Define the services that make up your app in docker-compose.yml so they can be run together in an isolated environment.
- Run "docker-compose up" and the Docker compose command starts and runs your entire app.
If we want to rebuild the container we can do it adding the "--build" parameter

```console
docker-compose up --build
```
