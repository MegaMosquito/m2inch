all: build run

build:
	docker build -t m2i_server .

dev: build stop
	-docker rm -f m2i_server 2> /dev/null || :
	docker run -it --privileged --name m2i_server -p 6667:6667 --volume `pwd`:/outside m2i_server /bin/bash

run: stop
	-docker rm -f speedtest 2>/dev/null || :
	docker run -d --privileged --name m2i_server -p 6668:6668 m2i_server

exec:
	docker exec -it m2i_server /bin/sh

stop:
	-docker rm -f m2i_server 2>/dev/null || :

clean: stop
	-docker rmi m2i_server 2>/dev/null || :

.PHONY: all build dev run exec stop clean
