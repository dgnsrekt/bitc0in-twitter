FROM python:3.7-slim-stretch AS base

ENV PYROOT /pyroot
ENV PYTHONUSERBASE $PYROOT


FROM base AS builder

RUN pip install pipenv

COPY Pipfile* ./

RUN PIP_USER=1 PIP_IGNORE_INSTALLED=1 pipenv install --system --deploy --ignore-pipfile


FROM base

COPY --from=builder $PYROOT/lib/ $PYROOT/lib/
COPY bitc0in_twitter bitc0in_twitter
COPY images images
COPY logme.ini logme.ini
COPY settings.ini settings.ini

COPY docker-entrypoint.sh docker-entrypoint.sh

RUN ["chmod", "+x", "./docker-entrypoint.sh"]

ENTRYPOINT ["./docker-entrypoint.sh"]
