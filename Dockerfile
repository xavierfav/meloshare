FROM ubuntu:latest
MAINTAINER Olivier Cervello "olivier.cervello@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential redis-server git
ADD ./nginx.conf /etc/nginx/conf.d/
COPY . /var/www/meloshare
WORKDIR /var/www/meloshare
RUN pip install -r requirements.txt
CMD ["supervisord -c supervisord.conf"]
