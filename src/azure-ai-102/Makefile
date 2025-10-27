SHELL := /bin/bash

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.ONESHELL:
genai-chat-rag-app-init: ## Initialize chat application
	cd genai || exit
	rm -r mslearn-ai-foundry -f
	git clone https://github.com/microsoftlearning/mslearn-ai-studio mslearn-ai-foundry
	# Copy updated lab files to running directory
	cp -f chat-app/* mslearn-ai-foundry/labfiles/chat-app/python/
	cp -f rag-app/* mslearn-ai-foundry/labfiles/rag-app/python/
	cd mslearn-ai-foundry
	rm -rf .git
	cd labfiles/chat-app/python
	uv sync
	cd ../../rag-app/python
	uv sync

.ONESHELL:
genai-chat-app-login-run: ## Login and Run chat application
	echo "Use browser for login"
	echo "Make sure to update the .env file using the endpoint information in Azure AI Foundry"
	az login
	cd ./genai/mslearn-ai-foundry/labfiles/chat-app/python/
	uv run chat-app.py

.ONESHELL:
genai-rag-app-login-run: ## Login and Run Retrieval Augmented Generation RAG application
	echo "Use browser for login"
	echo "Make sure to update the .env file using information in Azure AI Foundry Overview area"
	az login
	cd ./genai/mslearn-ai-foundry/labfiles/rag-app/python/
	uv run rag-app.py
