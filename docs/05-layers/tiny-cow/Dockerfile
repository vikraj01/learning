# Stage 1: a big image with the Go tools, only to build the program
FROM golang:1.25 AS build
WORKDIR /src
COPY main.go .
RUN CGO_ENABLED=0 go build -o cow main.go

# Stage 2: start from nothing, and copy in only the finished program
FROM scratch
COPY --from=build /src/cow /cow
ENTRYPOINT ["/cow"]
