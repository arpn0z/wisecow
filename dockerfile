FROM ubuntu:latest

# Prevent tzdata from prompting for input
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Kolkata

RUN apt-get update && \
    apt-get install -y tzdata fortune-mod cowsay netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

COPY wisecow.sh /app/wisecow.sh
WORKDIR /app
RUN chmod +x wisecow.sh

EXPOSE 4499
CMD ["bash", "wisecow.sh"]
