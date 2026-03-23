SHELL := /bin/bash

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.ONESHELL:
1-init: ## Initialize files from lab repo
	rm -rf mslearn-azure-ml
	uv sync
	git clone https://github.com/MicrosoftLearning/mslearn-azure-ml.git mslearn-azure-ml
	# Copy updated lab files to running directory inside mslearn-azure-ml
	cd mslearn-azure-ml
	rm -rf .git

1-run-code: Login-Notification ## Run code for labs
	az login
	# Alternatively, use uv run jupyter notebook
	uv run code ../../

.PHONY:
.ONESHELL:
Login-Notification:
	echo "Use browser for login"

