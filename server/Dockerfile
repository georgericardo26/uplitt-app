FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y libpq-dev \ 
    build-essential \
    gdal-bin \ 
    proj-bin
RUN mkdir -p /code
WORKDIR /code
COPY requirements.txt ./
RUN pip install -r requirements.txt
