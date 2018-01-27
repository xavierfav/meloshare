# Meloshare
Collaborative music sketching web application

## Installation
### Clone the repository
```
git clone https://github.com/xavierfav/meloshare
```

### Install the dependencies
```
pip install -r requirements.txt
```

### Install and run Redis
```
apt install redis-server
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
