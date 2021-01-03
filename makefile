#all:
	#docker-compose up

# HELP
# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help

help: ## This is help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

# DOCKER TASKS

# Build the container
build: ## Build the release and development container.
	docker-compose build --no-cache $(COMPOSE_PROJECT_NAME)
	docker-compose run $(COMPOSE_PROJECT_NAME) grunt build
	docker build -t $(COMPOSE_PROJECT_NAME) .

run: ## Run the container after build
	docker-compose up

# Build and run the container
up: ## Spin up the project
	docker-compose up --build $(COMPOSE_PROJECT_NAME)

stop: ## Stop running containers
	docker stop $(COMPOSE_PROJECT_NAME)

rm: stop ## Stop and remove running containers
	docker rm $(COMPOSE_PROJECT_NAME)

clean: ## Clean the generated/compiles files
	echo "nothing to clean..."
	#docker rm Structured.log