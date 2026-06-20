# DummyJSON Performance Tests

Projeto desenvolvido para a disciplina de Testes e qualidade de Software utilizando Locust e Docker.

## Sistema Testado

DummyJSON

https://dummyjson.com/


## Objetivo

Avaliar o comportamento da API DummyJSON sob diferentes níveis de carga, analisando:

- Tempo de resposta
- Throughput (req/s)
- Percentis (p90 e p95)
- Escalabilidade


## Cenários de Teste

- Listar Produtos (GET)
- Consultar produtos (GET)
- Listar Usuários (GET)
- Login (POST)
- Criar Postagem (POST)


## Tecnologias Utilizadas

- Python
- Locust
- Docker
- Matplotlib
- Reportlab


## Executando o Projeto

Subir o Locust:

```bash
docker compose up
```

Acessar:

```text
http://localhost:8089
```

---

## Testes Headless

Para executar os testes, basta utilizar os 3 comandos abaixo.

### 10 usuários

```bash
docker exec -it locust locust \
-f /mnt/locust/locustfile.py \
--headless \
-u 10 \
-r 2 \
--run-time 1m \
--csv=/mnt/locust/results_10
```

### 50 usuários

```bash
docker exec -it locust locust \
-f /mnt/locust/locustfile.py \
--headless \
-u 50 \
-r 5 \
--run-time 1m \
--csv=/mnt/locust/results_50
```

### 100 usuários

```bash
docker exec -it locust locust \
-f /mnt/locust/locustfile.py \
--headless \
-u 100 \
-r 10 \
--run-time 1m \
--csv=/mnt/locust/results_100
```

---

## Arquivos Gerados

Após cada execução:

```text
results_10_stats.csv
results_10_failures.csv
results_10_exception.csv
results_10_stats_history.csv

results_50_stats.csv
results_50_failures.csv
results_50_exception.csv
results_50_stats_history.csv

results_100_stats.csv
results_100_failures.csv
results_100_exception.csv
results_100_stats_history.csv
```

## Gerando relatório dinâmico

```bash
docker exec -it locust python relatorio.py
```
