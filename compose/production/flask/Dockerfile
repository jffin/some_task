FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

ARG USER_NAME="user"

ENV USER_NAME ${USER_NAME}
ENV CONTAINER_IMAGE_VER=v1.0.1

WORKDIR /code

RUN apt update && apt install -y gcc g++

RUN python -m pip install --upgrade pip

COPY ./requirements.txt setup.py ./
RUN python -m pip install -r requirements.txt
RUN python -m pip install -e .

RUN python -c "import nltk; nltk.download('punkt')"

COPY ./text_api text_api/
COPY ./migrations migrations/

RUN mkdir db

RUN apt purge -y gcc g++

RUN useradd ${USER_NAME} -s /sbin/nologin

RUN chown -R ${USER_NAME}:${USER_NAME} /code

USER ${USER_NAME}
