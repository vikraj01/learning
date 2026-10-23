FROM golang:1.25
WORKDIR /src
COPY main.go .
RUN CGO_ENABLED=0 go build -o cow main.go
ENTRYPOINT ["/src/cow"]
