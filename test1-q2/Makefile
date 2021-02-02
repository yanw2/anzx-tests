# use some sensible default shell settings
SHELL := /bin/bash -o pipefail
.SILENT:
.DEFAULT_GOAL := help

# default variables
IMAGE_NAME = anz-status-api
IMAGE_VERSION ?= $(shell git rev-parse --short HEAD)

##@ Entry Points
.PHONY: build
build: ## Build docker image artifact
	docker build -f Dockerfile . -t $(IMAGE_NAME)
	docker tag $(IMAGE_NAME):latest $(IMAGE_NAME):$(IMAGE_VERSION)

.PHONY: run 
run: ## Run API server image
	docker run $(IMAGE_NAME):$(IMAGE_VERSION)

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
