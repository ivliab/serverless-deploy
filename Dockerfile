FROM busybox as serverless
RUN wget -O /serverless https://github.com/serverless/serverless/releases/download/v2.9.0/serverless-linux-x64 && \
    chmod +x /serverless

FROM python:3.8-slim-buster

COPY --from=serverless /serverless /usr/local/bin/serverless

RUN apt-get update && apt-get install -y npm

COPY entrypoint.py /entrypoint.py

ENTRYPOINT ["/entrypoint.py"]
