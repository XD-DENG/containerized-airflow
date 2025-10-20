## Command to build image

Code here would ONLY fit **testing** or **demo** purposes.

```bash
docker build -t xddeng/airflow:airflow3 .
```

## Launch with `docker compose`

```bash
docker compose -p airflow_demo -f docker-compose.yml up --force-recreate --always-recreate-deps
```


## Demo Credentials

### Postgres
ID: `postgres`
Password: `password`
DB: `postgres`
