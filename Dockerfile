FROM python:3.8-buster AS base

WORKDIR /usr/src/site

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP wsgi.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT=3000
ENV GUNICORN_WORKERS=1
ENV GUNICORN_THREADS=5
ENV APP_CONFIG_FILE config.py

EXPOSE ${FLASK_RUN_PORT}

FROM base AS production
# for further information:
# https://docs.gunicorn.org/en/stable/design.html#how-many-workers
# https://stackoverflow.com/a/41696500
CMD gunicorn --bind :${FLASK_RUN_PORT} --workers ${GUNICORN_WORKERS} --threads ${GUNICORN_THREADS} "www.rodrigo.engineer:create_site()"

# CMD ["flask", "run"]