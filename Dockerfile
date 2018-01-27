FROM ubuntu:latest
MAINTAINER Olivier Cervello "olivier.cervello@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["supervisord"]
CMD ["supervisord -c supervisord.conf"]
