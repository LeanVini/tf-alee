#!/bin/sh
# Script para gerar certificados SSL self-signed
docker run --rm -v "$(pwd)/nginx/ssl":/ssl -w /ssl alpine sh -c "
  apk add --no-cache openssl &&
  openssl req -x509 -nodes -days 365 -newkey rsa:2048 \\
    -keyout key.pem \\
    -out cert.pem \\
    -subj '/C=BR/ST=SP/L=SP/O=Ecommerce/CN=localhost'
"
echo "Certificados SSL gerados em nginx/ssl/"

