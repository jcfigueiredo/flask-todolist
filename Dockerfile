FROM alpine:3.8

# from https://github.com/frol/docker-alpine-python3
RUN apk update && apk upgrade && \
    apk add --no-cache python3-dev && \
    apk add --no-cache gcc postgresql-dev musl-dev  && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

RUN pip install gunicorn

ADD requirements.txt /code/requirements.txt

WORKDIR /code

RUN pip install -r requirements.txt

ADD . /code