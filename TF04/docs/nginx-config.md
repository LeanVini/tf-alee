# Configuração Nginx - Load Balancer Avançado

## Upstream Backend
```
upstream backend_servers {
    least_conn;              # Algoritmo de balanceamento
    keepalive 32;            # Conexões persistentes
    
    server backend1:5000 max_fails=3 fail_timeout=30s weight=10;
    server backend2:5000 max_fails=3 fail_timeout=30s weight=8;
    server backend3:5000 max_fails=3 fail_timeout=30s weight=12;
}
```

## Health Checks
- `max_fails=3`: 3 falhas consecutivas
- `fail_timeout=30s`: Timeout por falha
- Health check Docker a cada 30s

## Rate Limiting
```
limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;
limit_req_zone $binary_remote_addr zone=frontend:10m rate=50r/s;
```

## Proxy Headers
```
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
```

## SSL/TLS
- Protocolos: TLSv1.2/1.3
- Ciphers fortes
- Certificado self-signed (gerado via Docker)

## Logs Detalhados
```
log_format main '... upstream=$upstream_addr upstream_response_time=$upstream_response_time';
```

