FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
ADD . /yaml_maker
WORKDIR /yaml_maker
COPY requirements.txt /yaml_maker
RUN pip install -r requirements.txt
COPY . /yaml_maker
