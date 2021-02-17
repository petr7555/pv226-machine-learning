FROM python:3.8-slim
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# not needed, works even without this
EXPOSE 5000
COPY api api
COPY model_autokeras model_autokeras

# Option 1) flask development server
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
# run from api directory, so that relative path to ../model_autokeras works
WORKDIR api
CMD ["flask", "run"]

# Option 2) gunicorn production server
#CMD ["gunicorn", "--chdir", "api", "main:app", "-b", "0.0.0.0:5000"]
