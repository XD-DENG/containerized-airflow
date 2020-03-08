## Command to build image

Code here would ONLY fit **testing** or **demo** purposes.

```bash
docker build -t xddeng/airflow:1.10.9_py36_localexecutor_postgres .
```

## Launch with `docker-compose`

```bash
docker-compose -p airflow_demo -f docker-compose.yml up -d
```


## Vanina Docker Commands to launch Airflow together with other services

```bash
docker network create -d bridge airflow-network

docker run \
    -d --network=airflow-network \
    -p 5432:5432 \
    --name db \
    -e POSTGRES_PASSWORD=password \
    postgres -c 'listen_addresses=*'

docker run \
    -d --network=airflow-network \
    -p 8000:8080 \
    --name adminer \
    adminer

docker run \
    -d --network=airflow-network \
    -p 8080:8080 \
    --name airflow \
    -e AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgres://postgres:password@db:5432/postgres \
    -e AIRFLOW__CORE__PARALLELISM=4 \
    -e AIRFLOW__WEBSERVER__EXPOSE_CONFIG=True \
    xddeng/airflow:1.10.9_py36_localexecutor_postgres

```

## Demo Credentials

### Postgres
ID: `postgres`
Password: `password`
DB: `postgres`

### Airflow
ID: `admin`
Password: `admin`