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

```sh
uv run projectfile.py

# or virtualenv activation
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r path/to/requirements.txt

```

### Running Application Scripts

See related README.md and Makefile for projects
and variables that must be set like using `.env`.

Most projects are run like `uv run main_project_file.py`

---

### Testing

- **Unit Test Structure:** There is no universal test runner or central pytest
  setup.

---

### Linting and Formatting

- No project-global lint config. Follow PEP8.
- To use formatters which are usully `black`, `ruff`
- To format with black:

  ```sh
  black .
  ```

- If ruff available, use:

  ```sh
  ruff .
  ```

---

## 2. Code Style Guidelines

### Indentation and Formatting

- Python files should use **2 spaces** per indent level ([.editorconfig]).
- Use spaces, NOT tabs. No trailing whitespace.
- Lines should generally adhere to **PEP8 max 79/89 char lines**.
- Group imports as:
  1. Standard library
  2. Third-party
  3. Local/app With a blank line between each group.
- Use absolute imports when possible.

### Naming Conventions

- Snake_case for variables, function_defs, and files.
- PascalCase for class names.
- Constants should be UPPER_SNAKE_CASE.
- Avoid non-descriptive or single-character names (except for looping/indexes).

### Typing and Function Signatures

- Prefer typing hints for arguments and return values (Python 3.6+):

  ```python
  def fetch_data(path: str, retries: int = 3) -> dict:
  ```

- Use `Any`, `Optional`, and other hints from `typing` where strict type cannot
  be determined.

### Docstrings and Comments

- Use triple-quoted docstrings for all public classes and functions:

  ```python
  def func(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b
  ```

- Add comments to clarify non-obvious logic

For Docstrings, use reStructuredText (PEP 287 defaut):

```python
def cast_spell(wand, incantation, target=None):
    """
    Cast a magical spell using a wand and incantation.
    This function simulates casting a spell. With no
    target specified, it is cast into the void.

    :param wand: The wand used to do the spell-casting deed.
    :type wand: str
    :param incantation: The words said to activate the magic.
    :type incantation: str
    :param target: The object or person the spell is directed at (optional).
    :return: A string describing the result of the spell.
    :rtype: str
```

### Error Handling

- Prefer narrow exception classes (not bare `except:` or raw `except Exception:`
  unless necessary).
- Use informative error messages and log as appropriate.
- Handle missing environment/config values gracefully and provide descriptive
  error output.

### Project Structure

- Code is separated by project inside `src/project/` and may
  have sub project folders
- Scripts should be named by their function or purpose
- When creating a new subproject, also provide a `README.md` and if needed
  `requirements.txt`/`pyproject.toml`

### Version Control

- Do NOT commit secrets or `.env` files. Respect the `.gitignore` settings (Python related)

### Third-party Libraries

- Use only listed dependencies. If additional ones are needed, update the local
  `requirements.txt` or `pyproject.toml` and document in the relevant README.
- `dotenv` is sometimes used for local environment variables in projects

### Security and Static Analysis

- CodeQL analysis is enabled in `.github/workflows/`. Avoid common security
  problems: do not shell out without sanitizing inputs, never expose secrets,
  and validate user inputs.

---

## 3. Adding Tests

- Place additional tests in proximity to the code or use a `tests` subdirectory.
- Follow test discovery conventions of your runner (`unittest`, `pytest`, etc).
- Add clear assert messages.

---

## 4. Additional Notes

- For questions about structure or best-practices, refer to
  [PEP8](https://peps.python.org/pep-0008/) and
  [Python Dev Guide](https://devguide.python.org/).
- No Cursor or Copilot specific rules as of now; follow these AGENTS guidelines
  and PEP8 conventions by default.
- Maintain these guidelines as the codebase and tooling evolve.

---

[.editorconfig]: .editorconfig
