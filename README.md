## GENERETING DOCKER IMAGE
#### CLONE THE REPO , ADD VARIABLES TO env_variables.env , and then run the following Docker commands:

```console
docker build -f Dockerfile -t app:latest .
docker run -p 5000:5000 app
```