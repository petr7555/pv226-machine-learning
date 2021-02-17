With help of https://docs.docker.com/compose/gettingstarted/.

Create virtual environment:

- `python -m venv venv`
- activate it with `source venv/bin/activate`

Install dependencies:
```
pip install flask pandas numpy autokeras tensorflow
```

Create `api` folder with `main.py`.

Inside `main.py`, have an `app` object.

Create `requirements.txt` by executing (pip is case-insensitive, so flask=Flask):
`pip freeze > requirements.txt`

Or list the dependencies manually (versions are inferred):
```
flask
pandas
numpy
autokeras
tensorflow
```

- Build container:
  `docker build -t titanic-api-image .`
- Run container:
  `docker run -d --name titanic-api -p 5000:5000 titanic-api-image`
- Stop and remove container:
  `docker kill titanic-api && docker rm titanic-api`
- or:
  `docker rm -f titanic-api`
- for all containers:
  `docker kill $(docker ps -q); docker rm $(docker ps -aq)`
- or (for all containers):
  `docker rm -f $(docker ps -aq)`

### Using docker compose instead of building separate container:
`docker compose up --build` (without `--build` option the image wouldn't be rebuilt)

Interactive terminal:
`docker exec -it <container_name> /bin/bash`

Use python:3.8-slim instead of python:3.8-alpine, 
because it is MUCH MUCH MUCH faster when installing pip dependencies.
Overall, the installation is still slow, because it needs almost 400 MB large tensorflow.
alpine also needs `RUN apk add --no-cache gcc musl-dev linux-headers` in Dockerfile

It is important to use `0.0.0.0`, not `127.0.0.1`, because of Docker.
