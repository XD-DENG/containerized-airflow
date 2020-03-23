## Command to build image

Code here would ONLY fit **testing** or **demo** purposes.

```bash
docker build -t xddeng/airflow:1.10.9_py36_celeryexecutor_postgres_redis .
```

## Launch with `docker-compose`

```bash
docker-compose -p airflow_demo -f docker-compose.yml up -d
```


## Demo Credentials

### Postgres
ID: `postgres`
Password: `password`
DB: `postgres`

### Airflow
ID: `admin`
Password: `admin`