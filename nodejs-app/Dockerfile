FROM ubuntu:14.04

RUN wget -qO- https://deb.nodesource.com/setup_4.x | sudo bash -
RUN apt-get update -y
RUN apt-get install nodejs -y
RUN apt-get install nodejs-legacy -y
RUN apt-get install npm -y

ADD . /app
WORKDIR /app

RUN npm install

CMD [ "npm", "start" ]

