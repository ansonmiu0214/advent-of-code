FROM python:3.13-alpine

ARG MODE='run'

RUN case "${MODE}" in               \
    "dev") apk add bash;;           \
    "test") pip install pytest;;    \
    esac

WORKDIR /workarea