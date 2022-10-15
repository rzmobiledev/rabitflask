FROM python:3.10.5-slim as base
LABEL maintainer="rzmobiledev@gmail.com"
ENV PYTHONUNBUFFERED 1

FROM base as builder
WORKDIR /install
COPY ./installer/requirements.txt .
COPY ./scripts /scripts

RUN apt update && pip install --upgrade pip && pip install --prefix="/install" -r requirements.txt && \
    adduser --no-create-home --disabled-password rizal && \
    chmod -R +x /scripts

USER rizal
FROM base
COPY --from=builder /install /usr/local
COPY --from=builder /scripts /usr/local/bin
COPY . /app
WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["command.sh"]