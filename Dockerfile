FROM ubuntu:latest
MAINTAINER Olivier Cervello "olivier.cervello@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential redis-server
COPY . /app
ADD ./nginx.conf /etc/nginx/conf.d/
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["supervisord -c supervisord.conf"]
