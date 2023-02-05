FROM python:3.10-slim-bullseye
ARG DEBIAN_FRONTEND=noninteractive
WORKDIR /weather-app
COPY . .
RUN apt update -y && apt install --no-install-recommends -y \
    build-essential \
    gcc \
    make \
    libpcap-dev \
    git \
    sudo \
    libtool \
    autoconf \
    pwgen \
    apache2 \
    iproute2 \
    libncurses5-dev \
    apache2-utils \
    nano \
    python3-csvkit \
    sshpass \
    git \
    openssl \
    curl \
    python3-pip \
    && pip install --upgrade pip \
       pip install -r ./requirements.txt
CMD ["python3", "weather_app.py"]