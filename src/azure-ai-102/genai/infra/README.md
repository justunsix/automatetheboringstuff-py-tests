# Infrastructure as Code for GenAI Labs

Create infrastructure for the
[Develop generative AI solutions in Azure](https://github.com/MicrosoftLearning/mslearn-ai-studio)
labs using Terraform.

## Infrastructure Requirements

- Azure Resource Group - hosts all other resources to be created
- Microsoft Foundry
- Microsoft Foundry project - named as {project_name}-resource

Recommended region by AI Foundry: `EastUS`,
fine tuning lab may require `North Central US` or `Sweden Central`.

### Other Optional resources

- Microsoft Foundry, deployed model `gpt-4-1`
