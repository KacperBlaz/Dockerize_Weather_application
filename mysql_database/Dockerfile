FROM mysql:8-debian
ARG DEBIAN_FRONTEND=noninteractive
WORKDIR /mysql
COPY . .
MAINTAINER kacperblaz@gmail.com
RUN apt update -y && apt install --no-install-recommends -y \
    net-tools
EXPOSE 3306/tcp
