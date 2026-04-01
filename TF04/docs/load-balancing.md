# Load Balancing - Alta Disponibilidade

## Algoritmo: least_conn
Distribui requisições para instância com **menor número de conexões ativas**.

## Pesos das Instâncias
| Instância | Weight | Load Factor |
|-----------|--------|-------------|
| backend1  | 10     | 1.0         |
| backend2  | 8      | 1.2         |
| backend3  | 12     | 0.8         |

## Failover Automático
1. Instância falha 3 health checks → removida do pool
2. Recupera após sucesso → reintegrada
3. Nginx monitora continuamente

## Teste de Distribuição
```bash
for i in {1..20}; do
  curl -s http://localhost/api/info | jq .instance_id
done
```

## Métricas de Performance
```
Active connections: X
Reading: Y   Writing: Z   Waiting: W
```

Endpoint: `http://localhost/nginx-status`

