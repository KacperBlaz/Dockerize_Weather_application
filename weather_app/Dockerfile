FROM python:3.10-slim-bullseye
ARG DEBIAN_FRONTEND=noninteractive
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
    python3-pip \
    && pip install --upgrade pip \
       pip install -r ./requirements.txt
CMD ["python3", "weather_app.py" ]