airflow initdb;
airflow create_user -r Admin -u admin -e admin@test.com -f xd -l deng -p admin;
airflow scheduler -D --stdout /dev/null --stderr /dev/null --pid $AIRFLOW_HOME/scheduler.pid -l $AIRFLOW_HOME/scheduler.log &
airflow webserver -D --stdout /dev/null --stderr /dev/null --pid $AIRFLOW_HOME/webserver.pid -l $AIRFLOW_HOME/webserver.log
