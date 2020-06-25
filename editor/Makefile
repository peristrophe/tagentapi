THIS := $(lastword $(MAKEFILE_LIST))
APP  := swaggerapi/swagger-editor
NAME := SwaggerEditor

.PHONY: fetch
fetch:
	docker pull $(APP)

.PHONY: clean
clean: stop
	docker rmi $(shell docker images $(APP) -q)

.PHONY: start
start: fetch
	docker run --rm -d -p 80:8080 --name $(NAME) $(APP)
	@echo
	@echo "ACCESS TO USE: http://localhost:80/"

.PHONY: stop
stop:
	docker container ls -qf name=$(NAME) | xargs docker stop

.PHONY: restart
restart: stop start ;
