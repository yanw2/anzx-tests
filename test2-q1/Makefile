# use some sensible default shell settings
SHELL := /bin/bash -o pipefail
.SILENT:
.DEFAULT_GOAL := help

# default variables
IMAGE_NAME = anz-golang-test
IMAGE_VERSION ?= $(shell git rev-parse --short HEAD)

##@ Entry Points
.PHONY: build
build: ## Build docker image artifact
	docker build . -t $(IMAGE_NAME)
	docker tag $(IMAGE_NAME):latest $(IMAGE_NAME):$(IMAGE_VERSION)

.PHONY: run
run: ## Run the docker image
	docker run -d -p 8000:8000 $(IMAGE_NAME):$(IMAGE_VERSION)

.PHONY: stop
stop: ## Stop and remove all running containers
	docker container ls -a -q | xargs docker container stop | xargs docker rm

.PHONY: test
test: ## Test the docker container
	curl http://127.0.0.1:8000

##@ Misc
.PHONY: help
help: ## Display this help
	awk \
	  'BEGIN { \
	    FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n" \
	  } /^[a-zA-Z_-]+:.*?##/ { \
	    printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 \
	  } /^##@/ { \
	    printf "\n\033[1m%s\033[0m\n", substr($$0, 5) \
	  }' $(MAKEFILE_LIST)

##@ Helpers
.PHONY: _clean
_clean: ## Clean all local images
	echo "Removing orphaned docker networks"
	docker-compose down --remove-orphans 2>/dev/null
