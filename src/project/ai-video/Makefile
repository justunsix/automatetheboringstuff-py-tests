SHELL := /bin/bash

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.ONESHELL:
run: ## Run CogVideo
	git clone https://github.com/THUDM/CogVideo.git
	cd "CogVideo/inference/gradio_composite_demo" || exit
	# On Ubuntu, install pillow dependencies
	sudo apt-get install libjpeg-dev zlib1g-dev
	uv venv
	uv pip install -r requirements.txt
	uv run app.py


