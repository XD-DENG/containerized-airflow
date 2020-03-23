FROM python:3.6-slim

ARG AIRFLOW_HOME=/usr/local/airflow

ENV AIRFLOW_HOME=${AIRFLOW_HOME}

# Use env variables for Airflow configuration
ENV AIRFLOW__WEBSERVER__RBAC=True
ENV AIRFLOW__CORE__EXECUTOR=LocalExecutor

RUN set -ex \
    && buildDeps=' \
        python3-dev \
        libkrb5-dev \
        libsasl2-dev \
        libssl-dev \
        libffi-dev \
        libblas-dev \
        liblapack-dev \
        libpq-dev \
    ' \
    && apt-get update -yqq \
    && apt-get upgrade -yqq \
    && apt-get install -yqq --no-install-recommends \
        $buildDeps \
        build-essential \
        python3-pip \
        apt-utils \
        locales \
    && sed -i 's/^# en_US.UTF-8 UTF-8$/en_US.UTF-8 UTF-8/g' /etc/locale.gen \
    && locale-gen \
    && update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 \
    && useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow \
    && pip install -U pip setuptools wheel \
    && apt-get purge --auto-remove -yqq $buildDeps \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf \
        /var/lib/apt/lists/* \
        /tmp/* \
        /var/tmp/* \
        /usr/share/man \
        /usr/share/doc \
        /usr/share/doc-base

RUN pip install psycopg2-binary
RUN pip install cryptography
RUN pip install 'apache-airflow==1.10.9'
RUN pip install 'apache-airflow[celery]==1.10.9'
RUN pip install 'apache-airflow[redis]==1.10.9'


# Set the working directory
WORKDIR ${AIRFLOW_HOME}

# Copy the current directory contents into the container at the working dir
COPY . ${AIRFLOW_HOME}

RUN chown -R airflow: ${AIRFLOW_HOME}
USER airflow

EXPOSE 8080

CMD ["bash", "start_airflow.sh"]
