SHELL := /bin/bash

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.ONESHELL:
configure-conda-environment-ds: ## Create conda environment for data-science and other projects
	cd src/project/data-science
	conda config --append channels conda-forge
	conda create --name "data-science" --file requirements.txt --yes
