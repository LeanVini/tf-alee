# TF04 - Ale

## Aluno
- **Nome:** Vinícius Caires De Souza
- **RA:** 6324613
- **Curso:** Análise e Desenvolvimento de Sistemas

## Arquitetura
- **Nginx:** Load balancer com SSL e rate limiting
- **Backend:** 3 instâncias da API para alta disponibilidade
- **Frontend:** Loja virtual estática
- **Admin:** Painel administrativo

## Funcionalidades Implementadas
- ✅ Load balancing com algoritmo least_conn
- ✅ Health checks automáticos
- ✅ Failover transparente
- ✅ SSL/TLS com certificado self-signed
- ✅ Rate limiting para proteção
- ✅ Logs detalhados com upstream info
- ✅ Compressão gzip
- ✅ Virtual hosts

## Como Executar

### Pré-requisitos
- Docker e Docker Compose

### Execução
```bash
cd TF04

# Gerar certificados SSL (se necessário)
docker run --rm -v %cd%\TF04\nginx\ssl:/ssl -w /ssl alpine sh -c "apk add openssl && openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout key.pem -out cert.pem -subj '/CN=localhost'"

# Subir todos os serviços
docker-compose up -d --build

# Verificar status
docker-compose ps
```

## Endpoints
- Frontend: http://localhost ou https://localhost
- API: http://localhost/api/
- Admin: http://localhost/admin/
- Status: http://localhost/nginx-status
- Health: http://localhost/health

## Testes de Load Balancing
```bash
# Testar distribuição de carga
for /L %i in (1,1,10) do curl -s http://localhost/api/info | findstr instance_id

# Simular falha de instância
docker-compose stop backend1

# Verificar failover
curl http://localhost/api/info
```

## Monitoramento
- Logs detalhados: `docker-compose logs nginx`
- Métricas: http://localhost/nginx-status
- Health checks automáticos a cada 30s

### Validação
```bash
cd TF04
docker-compose up -d --build
for /L %i in (1,1,6) do curl -s http://localhost/api/info
docker-compose down
```

