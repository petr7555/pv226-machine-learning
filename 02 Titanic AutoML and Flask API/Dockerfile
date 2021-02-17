#FROM python:3.7-alpine
FROM python:3.8-slim
WORKDIR /code
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
#RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY api api
COPY model_autokeras model_autokeras

# run from api directory, so that relative path to ../model_autokeras works
WORKDIR api
CMD ["flask", "run"]
