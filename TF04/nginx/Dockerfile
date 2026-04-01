FROM nginx:alpine

# Copiar configurações
COPY nginx.conf /etc/nginx/nginx.conf
COPY conf.d/ /etc/nginx/conf.d/
COPY ssl/ /etc/nginx/ssl/

# Criar diretório para frontend
RUN mkdir -p /usr/share/nginx/html/frontend

# Expor portas
EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]

