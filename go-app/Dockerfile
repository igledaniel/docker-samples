FROM golang

ADD . /go/src/github.com/mapzen/goexample

RUN go get github.com/codegangsta/gin

WORKDIR /go/src/github.com/mapzen/goexample

EXPOSE 8080
