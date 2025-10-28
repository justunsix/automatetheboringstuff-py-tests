SHELL := /bin/bash

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.ONESHELL:
1-genai-chat-rag-app-init: ## Initialize chat and RAG application files from external repo
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

.PHONY:
.ONESHELL:
Login-Notification:
	echo "Make sure to update the .env file using the endpoint information in Azure AI Foundry"
	echo "Use browser for login"

.ONESHELL:
2a-genai-chat-app-login-run: Login-Notification ## Login and Run chat application
	az login
	cd ./genai/mslearn-ai-foundry/labfiles/chat-app/python/
	uv run chat-app.py

.ONESHELL:
2b-genai-rag-app-login-run: Login-Notification ## Login and Run Retrieval Augmented Generation RAG application
	az login
	cd ./genai/mslearn-ai-foundry/labfiles/rag-app/python/
	uv run rag-app.py

3-agents-develop-ai-agent-init: ## Initialize agent files from external repo
	cd agents || exit
	rm -r ai-agents -f
	git clone https://github.com/MicrosoftLearning/mslearn-ai-agents ai-agents
	cp -f 02-build-ai-agent/* ai-agents/Labfiles/02-build-ai-agent/Python/
	cd ai-agents
	rm -rf .git
	cd Labfiles/02-build-ai-agent/Python
	uv sync

4a-agents-develop-ai-agent-run: Login-Notification ## Login and Run agent with Code interpreter and threads
	az login
	cd ./agents/ai-agents/Labfiles/02-build-ai-agent/Python/
	uv run agent.py

