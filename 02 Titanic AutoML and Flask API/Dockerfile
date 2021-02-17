FROM python:3.8-slim
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY api api
COPY model_autokeras model_autokeras

WORKDIR api
CMD ["python", "main.py"]
