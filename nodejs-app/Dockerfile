FROM mhart/alpine-node

ADD . /app
WORKDIR /app

RUN npm shrinkwrap

CMD [ "npm", "start" ]

