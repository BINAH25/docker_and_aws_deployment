FROM python:3.11.4-alpine
WORKDIR /apps
COPY ./my_app ./
RUN pip install --upgrade pip --no-cache-dir
RUN apk add --no-cache postgresql-dev
# Install additional dependencies for building psycopg2
RUN apk add --no-cache musl-dev gcc
# Install Python dependencies
RUN pip install -r /apps/requirements.txt --no-cache-dir

#CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
CMD ["gunicorn","main_app.wsgi:application","--bind","0.0.0.0:8000"]