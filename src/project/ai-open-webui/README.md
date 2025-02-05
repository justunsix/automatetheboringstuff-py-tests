# open-webui and local AI tests

## Prerequisites

- [Ollama](https://github.com/ollama/ollama/) - run local large language models (LLM)
- [open-webui](https://github.com/open-webui/open-webui) - LLM wrapper
- Python
  - Optionally use `uv` for virtual environment and dependency management

## Usage

```shell
# Run open-webui per its documentation
# If you have `uv`, can run `make run` or
uv run open-webui serve

# Serve ollama
ollama serve
ollama run <your_desired_model>
```
