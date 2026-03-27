SHELL := /bin/bash

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

tf-init: ## Initialize Terraform project
	# Initilize the terraform project
	terraform init
	# Upgrade the terraform project
	terraform init -upgrade

az-login: ## Login to Azure
	## Required otherwise Terraform plan can generate errors like "marshaling: string field contains invalid UTF-8"
	## Choose subscription: <subscription_id>
	az login
	az account set --subscription $(ARM_SUBSCRIPTION_ID)

tf-format-and-validate: ## Format and validate Terraform files
	# Format the terraform files
	terraform fmt
	# Validate the terraform files
	terraform validate

tf-plan: ## Plan Terraform deployment and output plan
	terraform plan -out=tfplan

tf-apply: ## Apply Terraform deployment and show
	terraform apply tfplan

tf-state: ## See state file and resources
	terraform state list

tf-destroy:	## Destroy Terraform deployment
	terraform destroy -auto-approve

tf-show: ## See state
	terraform show	

tf-all: tf-init az-login tf-format-and-validate tf-plan tf-apply ## Initialize project, login to Azure, Set up Terraform and Apply Configuration

tf-apply-changes: tf-format-and-validate tf-plan tf-apply ## Apply changes made to configuration to Terraform deployment
