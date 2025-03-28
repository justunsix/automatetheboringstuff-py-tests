# About this Folder

Projects by folder:

- `automation-gpt` - ChatGPT API interaction using python
  - `python-chatgpt` - API call to ChatGPT to generate Python code to automate
    tasks
- `csv` - Working with `csv` files
  - `compare-columns` - Compare two columns in a `csv` file and file same and
    different values in the two columns
  - `reorder-names` - Reorder names / field data in a `csv` file in an order
    specified in the file
- `data-science` - data analysis and management
  - Handle searching, replacing, querying, viewing, and editing data
- `diagrams` - Creating diagrams as code using `diagrams` python package
- `kubernetes` - Managing kubernetes (k8s) resources
- `scan-keywords`
  - `scan-keywords` - Scan keywords, metadata in files and create an output on
    results (for example reports)

## Environment Setup

For projects with a `requirements.txt` file, use the following commands to setup
a virtual environment and install dependencies:

```sh
# Install dependencies in a virtual environment
python -m venv ./venv
# Activate virtual environment
./venv/Scripts/activate
# or in PowerShell
# ./venv/Scripts/Activate
pip install -r requirements.txt
```
