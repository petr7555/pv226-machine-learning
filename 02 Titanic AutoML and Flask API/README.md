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

Create `runtime.txt` with python version, for example:
`python-3.8.7` (find out python version by running `python --version`)

Create `Procfile` with `gunicorn --chdir api main:app`.
We change directory to `api`, because that is where `main.py` is. 
`app` is the name of our Flask object.

Create Dockerfile in root folder with contents:
```
FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./api /app
```
Destination directory must be /app.

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
- or:
  `docker rm -f $(docker ps -aq)`

### Using docker compose instead of building separate container:
`docker compose up --build` (without --build option the image wouldn't be rebuilt)

Interactive terminal:
`docker exec -it <container_name> /bin/bash`

Using python:3.7-slim instead of python:3.7-alpine, 
because it is MUCH faster to install pip dependencies.
`RUN apk add --no-cache gcc musl-dev linux-headers` is then removed, when using slim.


TODO:
try original but without apk
add tensorflow to requirements.txt
gunicorn
