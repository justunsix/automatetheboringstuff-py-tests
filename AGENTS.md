# AGENTS.md

## Repository Automation, Style, and Command Reference for Agentic Coding Agents

---

This guide is for code generation, testing, linting, and maintenance by agentic
systems and developer agents working within `automatetheboringstuff-py-tests`.
It has whole codebase and per project rules for command usage, code style,
structure, and best practices.

---

## 1. Build, Lint, and Test Commands

### Python Environment

- Python version: **3.12+ recommended**, see individual `pyproject.toml` or
  `requirements.txt` for dependencies.
- Projects are in subfolders. If `pyproject.toml` is present use `uv run` to
  both install dependencies and run programs.
  Alternatively, activate a virtual environment and install
  the appropriate `requirements.txt` or `pyproject.toml` as needed
  or simply use `uv run`. Example:

### Running Scripts

If `pyproject.toml` is present, use `uv run` to install deps and execute:

```sh
uv run <script>.py
```

For legacy projects with `requirements.txt`:

```sh
python -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt
python <script>.py
```

Some projects have Makefiles with self-documenting targets (search for `##`):

```sh
make help             # list available targets
make <target-name>    # run a target
```

See each sub-project's `README.md` for required environment variables (`.env`).

### Linting and Formatting

Format with `black` and lint with `ruff`. Run from repo root or sub-project dir:

```sh
black .    # auto-format Python files
ruff .     # lint (default rules)
```

No project-global config exists for these tools; they use defaults.

### Testing

There is **no test infrastructure** in this repository. No `test_*.py` files,
no `pytest.ini`, no `conftest.py`, no test dependencies.

When adding tests, follow these conventions:

- Use `pytest` as the test runner.
- Place tests in a `tests/` subdirectory adjacent to the code, or name files
  `test_<module>.py`.

---

## 2. Code Style Guidelines

### Indentation and Formatting

- Use **2 spaces** per indent level ([.editorconfig]).
- Spaces only, no tabs. No trailing whitespace.
- Keep lines within **79 characters** (soft limit) or **89 characters** (hard).
- Use f-strings for string formatting preferred over `.format()`.

### Imports

Group imports in this order with a blank line between each group:

1. Standard library
2. Third-party packages
3. Local / relative imports

```python
import sys
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv

from config import settings
```

Use absolute imports when possible. Avoid wildcard imports (`from x import *`).

### Naming Conventions

- `snake_case` for variables, functions, and module filenames.
- `PascalCase` for class names.
- `UPPER_SNAKE_CASE` for constants and script-level configuration.
- Avoid single-character names except for loop indexes and simple comprehensions.

### Typing and Function Signatures

Add type hints for arguments and return values:

```python
def fetch_data(path: str, retries: int = 3) -> dict:
```

Use `Any`, `Optional`, `Union`, etc. from `typing` when strict types are not
possible. Use `None` sentinel pattern for optional args with `Optional[T]`.

### Docstrings and Comments

Use triple-quoted docstrings for all public functions and classes.
Default to reStructuredText style (PEP 287):

```python
def check_csv_encoding(csv_file: str) -> None:
  """
  Check the encoding of a CSV file by decoding each line with UTF-8.

  :param csv_file: Path to the CSV file.
  :type csv_file: str
  :return: None. Prints error messages if encoding issues are found.
  :rtype: None
  """
```

Add inline comments only for non-obvious logic.

### Error Handling

- Catch narrow exception classes, not bare `except:` or broad `except Exception`
  unless at a top-level script entry point.
- Provide informative error messages with context.
- For CLI scripts, handle missing env vars gracefully:

```python
api_key = os.getenv("API_KEY")
if not api_key:
  print("Error: API_KEY environment variable is not set.", file=sys.stderr)
  sys.exit(1)
```

### Script Entry Points

Prefer a `def main()` pattern with a guard:

```python
def main() -> None:
  ...

if __name__ == "__main__":
  main()
```

### Security and Static Analysis

- CodeQL analysis is enabled in `.github/workflows/`. Avoid common security
  problems: do not shell out without sanitizing inputs, never expose secrets,
  and validate user inputs.

### Project Structure

- Code is organized under `src/` by domain:
  - `src/project/` -- general-purpose Python projects (CSV, data science,
    web automation, AI/LLM tools, etc.)
  - `src/azure-ai-102/` -- Azure AI-102 certification study code
  - `src/azure-dp-100/` -- Azure DP-100 certification study code
  - `src/learn/` -- learning notes and small exercises
- Each sub-project should have a `README.md` and either `pyproject.toml` or
  `requirements.txt` listing its dependencies.
- Use kebab-case for script filenames: `csv-check-duplicates.py`.

### Version Control

- Never commit secrets, `.env` files, or API keys.
- Respect the `.gitignore` (Python, IDE, virtual env patterns).
- CodeQL security analysis runs weekly via GitHub Actions. Avoid shell injection
  risks and validate all user inputs.

### Third-party Libraries

- Only use dependencies listed in the relevant `pyproject.toml` or
  `requirements.txt`. If a new dependency is needed, add it there first.
- `python-dotenv` is used in some projects for environment variables.
- No project-global dependency file exists; each sub-project manages its own.

---

## 3. References

- [PEP 8 -- Style Guide](https://peps.python.org/pep-0008/)
- [PEP 257 -- Docstring Conventions](https://peps.python.org/pep-0257/)
- [Python Developer's Guide](https://devguide.python.org/)
- No Cursor rules (`.cursorrules` / `.cursor/rules/`) or Copilot instructions
  (`.github/copilot-instructions.md`) exist. Follow this document and PEP 8.

---

[.editorconfig]: .editorconfig
