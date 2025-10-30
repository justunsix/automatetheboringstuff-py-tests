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

4a-agents-develop-ai-agent-run: Login-Notification ## Login and Run agent with Code interpreter and threads
	az login
	cd ./agents/ai-agents/Labfiles/02-build-ai-agent/Python/
	uv run agent.py

4b-agents-multi-agent-solution-run: Login-Notification ## Login and Run agent with multiple agents
	az login
	cd ./agents/ai-agents/Labfiles/03b-build-multi-agent-solution/Python
	uv run agent_triage.py

5-language-init: ## Initialize language files from external repo
	cd language || exit
	rm -r mslearn-ai-language -f
	git clone https://github.com/microsoftlearning/mslearn-ai-language
	cp -f 01-analyze-text/* mslearn-ai-language/Labfiles/01-analyze-text/Python/text-analysis/
	cp -f 02-qna/* mslearn-ai-language/Labfiles/02-qna/Python/qna-app
	cp -f 04-text-classification/* mslearn-ai-language/Labfiles/04-text-classifications/Python/classify-text
	cp -f 09-audio-chat/* mslearn-ai-language/Labfiles/09-audio-chat/Python/
	cd mslearn-ai-language
	rm -rf .git

6a-language-01-analyze-text: ## Run text analysis
	cd ./language/mslearn-ai-language/Labfiles/01-analyze-text/Python/text-analysis/ || exit
	uv run text-analysis.py

6b-language-02-qna: ## Run question and answering chat
	cd ./language/mslearn-ai-language/Labfiles/02-qna/Python/qna-app/ || exit
	uv run qna-app.py

6c-language-04-classify-text: ## Run text classification
	cd ./language/mslearn-ai-language/Labfiles/04-text-classification/Python/classify-text || exit
	uv run classify-text.py

6d-language-09-audio-chat: Login-Notification ## Run audio chat
	az login
	cd ./language/mslearn-ai-language/Labfiles/09-audio-chat/Python/ || exit
	uv run audio-chat.py

7-vision-init: ## Initialize vision files from external repo
	cd vision
	rm -r mslearn-ai-vision -f
	git clone https://github.com/MicrosoftLearning/mslearn-ai-vision
	cp -f analyze-images/* mslearn-ai-vision/Labfiles/analyze-images/python/image-analysis/
	cp -f face/* mslearn-ai-vision/Labfiles/face/python/face-api/
	cd mslearn-ai-vision
	rm -rf .git

8a-vision-analyze-images: ## Run analyze images
	cd ./vision/mslearn-ai-vision/Labfiles/analyze-images/python/image-analysis/ || exit
	uv run image-analysis.py images/street.jpg
	# uv run image-analysis.py images/building.jpg
	uv run image-analysis.py images/person.jpg

8b-vision-face: ## Run facial services
	cd ./vision/mslearn-ai-vision/Labfiles/face/python/face-api/ || exit
	uv run analyze-faces.py images/face1.jpg
