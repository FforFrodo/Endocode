#all:
	#docker-compose up

# HELP
# This will output the help for each task
.PHONY: help

help: ## This is help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

# DOCKER TASKS

# Build the container
build: ## Build the development container.
	docker-compose build --no-cache $(COMPOSE_PROJECT_NAME)
	docker-compose run $(COMPOSE_PROJECT_NAME) grunt build
	docker build -t $(COMPOSE_PROJECT_NAME) .

run: ## Run the container after build
	docker-compose up

up: ## Build and run the container
	docker-compose up --build $(COMPOSE_PROJECT_NAME)

stop: ## Stop running container
	docker stop $(COMPOSE_PROJECT_NAME)

rm: stop ## Stop and remove running containers
	docker rm $(COMPOSE_PROJECT_NAME)

clean: ## Delete the log file
	rm Structured.log
	echo "nothing to clean..."