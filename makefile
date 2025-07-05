# Makefile for managing Airflow with Docker

# Initialise the Airflow metadata DB and create admin user
init:
	docker compose run webserver airflow db init
	docker compose run webserver airflow users create \
	  --username airflow \
	  --password airflow \
	  --firstname user \
	  --lastname User \
	  --role Admin \
	  --email your@email.com

# Start Airflow webserver and scheduler
start:
	docker compose up

# Stop all running containers
stop:
	docker compose down

# Restart everything cleanly
restart: stop start

# Remove all containers, volumes, and reset DB
reset:
	docker compose down -v
	rm -rf ./dags/__pycache__








# Access UI: http://localhost:8080
# Login: airflow / airflow