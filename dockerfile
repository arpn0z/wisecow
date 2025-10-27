FROM ubuntu:20.04

# Install dependencies
RUN apt-get update && \
    apt-get install -y fortune-mod cowsay netcat-openbsd nginx openssl && \
    rm -rf /var/lib/apt/lists/*

# Copy app
WORKDIR /app
COPY wisecow.sh .
COPY nginx.conf /etc/nginx/nginx.conf

# Generate a self-signed TLS certificate
RUN mkdir -p /etc/nginx/ssl && \
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/nginx/ssl/server.key \
    -out /etc/nginx/ssl/server.crt \
    -subj "/CN=localhost"

# Expose HTTPS port
EXPOSE 443

# Start both services: Wisecow + NGINX
CMD bash -c "/app/wisecow.sh & nginx -g 'daemon off;'"
