Create api folder with main.py. (must be named main.py)
Create virtual environment in api:
- `python -m venv venv`
- activate it with `source venv/bin/activate`

Install dependencies:
```
pip install flask pandas autokeras
```
Inside main.py, have app object (must be named app)
Create Dockerfile in root folder with contents:
```
FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./api /app
```
Destination directory must be /app.
Build container:
`docker build -t titanic-api .`
Run container:

Delete old container
`docker rm -f titanic-api`
