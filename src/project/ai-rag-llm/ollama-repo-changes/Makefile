SHELL := /bin/bash

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.ONESHELL:
1-setup-py-environment: ## Set up Python environment and install dependencies
	python -m venv .venv
	source .venv/bin/activate 
	pip install -r requirements.txt

.ONESHELL:
3-run-chatbot: ## Run the chatbot
	# Set env variable INIT_INDEX which determines weather needs to create the index
	export INIT_INDEX=true	
	source .venv/bin/activate
	.venv/bin/python api.py

.ONESHELL:
4-test-chatbot: ## Test the chatbot with question
	curl -i -XPOST "http://localhost:7654/api/question" \
	--header "Content-Type: application/json" \
	--data '
	{
	"question": "what is RAG stand for",
	"user_id": "user1"
	}
	'
4.1-test-chatbot: ## Test the chatbot with question
	curl -i -XPOST "http://localhost:7654/api/question" \
	--header "Content-Type: application/json" \
	--data '
	{
	"question": "What are good AI tools other than ChatGPT?",
	"user_id": "user1"
	}
	'

4.2-test-chatbot: ## Test the chatbot with a user-provided question
    @read -p "Enter your question: " question; \
    curl -i -XPOST "http://localhost:7654/api/question" \
    --header "Content-Type: application/json" \
    --data "$$(
        cat <<-EOF
        {
            "question": "$$question",
            "user_id": "user1"
        }
        EOF
    )"