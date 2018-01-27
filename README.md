# Meloshare
Collaborative music sketching web application.
Built using Python Flask, Flask-Flash, Celery and Redis.

## Quickstart (Docker)
You'll need to have `docker` and `docker-compose` installed.

**Note:** To get a compatible docker-compose, don't use `yum` to install it.
As sudo user, type:
```
rm /usr/bin/docker-compose
curl -L https://github.com/docker/compose/releases/download/1.11.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```

Now you can run the docker-compose.yml file in the root directory of the app:
```
docker-compose up
```

Run it in background by using `docker-compose up -d` (detached).

Tail the logs by using `docker-compose`.

## Quickstart
Let's clone the repo, create a virtualenv, install the pip requirements and run our application.

In a terminal (Ubuntu here):

```
# Get the code
git clone https://github.com/xavierfav/meloshare

# Create virtualenv
mkvirtualenv meloshare # Note: You can also use the command `virtualenv venv`.

# Install pip dependencies
pip install -r requirements.txt 

# Install Redis
apt install redis-server 

# Run supervisor
supervisord -c supervisord.conf # run all services

# Administrate services (stop, start, restart, reload, ...)
supervisorctl 
```

After running the above steps the following services should be RUNNING in `supervisorctl` shell:
- `ui`  --> User interface (port 5000)
- `api` --> Application programming interface (port 5001)
- `worker` --> Celery worker processing tasks
- `scheduler` --> Celery scheduler for periodic tasks
- `redis` --> Redis server (API caching for GET requests)

Supervisor allows you to administrate the services from the shell with the commands: `status <service>`, `start <service>`, `stop <service>`, `restart <service>`, or `tail -f <service>`.

You can also use `start/stop/status all` to control all services.

You can pass a space-separated list of services to control multiple simultaneously.

You can reload the supervisor configuration and update the running processes: `reread` and then `update`.

## Running services manually

Supervisor is merely running commands for you and control the life of your processes.
The following shows which command is run by supervisor for each service.

### Run Redis
```
redis-server
```

### Run the UI
```
FLASK_APP=meloshare/ui/app.py flask run
```

### Run the API
```
FLASK_APP=meloshare/api/app.py flask run
```

### Run the worker
```
celery worker -A meloshare.celeryapp:app -l info
```
