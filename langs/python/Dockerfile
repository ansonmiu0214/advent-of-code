FROM python:3.13-alpine

RUN apk add bash

ARG MODE='run'
RUN case "${MODE}" in               \
    "test") pip install pytest;;    \
    esac

WORKDIR /workarea