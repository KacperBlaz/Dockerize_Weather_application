FROM python:3.10-slim-bullseye
ARG DEBIAN_FRONTEND=noninteractive
ENV SQLALCHEMY_SILENCE_UBER_WARNING=1
WORKDIR /app
COPY . .
RUN apt update -y && apt install --no-install-recommends -y \
    build-essential \
    libpcap-dev \
    sudo \
    nano \
    python3-csvkit \
    sshpass \
    curl \
    net-tools \
    python3-pip \
    iputils-ping \
    && pip3 install --upgrade pip \
       pip3 install -r ./weather_app/requirements.txt
ENTRYPOINT ["python3", "weather_app.py" ]