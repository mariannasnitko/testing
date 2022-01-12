FROM python:latest
ARG PORT
ENV SERVER_PORT=$PORT
COPY server.py /
RUN mkdir /data
ENTRYPOINT python3 server.py $SERVER_PORT