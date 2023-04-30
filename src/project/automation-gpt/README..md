# Python Automation with ChatGPT

Following demonstration at [Python Automation with ChatGPT](https://www.youtube.com/watch?v=w-X_EQ2Xva4) by TechWorld with Nana.

## Built With

Prerequisites needed to run project.

- [OpenAI API](https://platform.openai.com/)
  - [OpenAI API Documentation](https://platform.openai.com/docs/introduction)
  - Create and save a new API key
  - Save key to environment variable `OPENAI_API_KEY`. To prevent the key from being stored in shell history, store the variable and key in a file and [use sourcing such as in bash and PowerShell](https://superuser.com/questions/71446/equivalent-of-bashs-source-command-in-powershell)
- [Python 3](https://www.python.org/) and pip (package installer for Python)
  - Libraries:
    - `requests` - http library
    - `bs4` - beautiful soup for working with webpages
    - `googletrans` - translate

## Getting Started

For the commands below use `python` or `python3` depending on your system's python binary.

### Pre-requisites

```sh
# Install dependencies in a virtual environment
python -m venv ./venv
# Activate virtual environment
./venv/Scripts/activate
# or in PowerShell
# ./venv/Scripts/Activate
pip install -r requirements.txt
```

## Usage

### OpenAI API Calls

```sh
# Get response from OpenAI and save response to file
python python-chatgpt.py "print today's date" "today_date.py"

# Example #1 from "Python Automation with ChatGPT" demonstration
python python-chatgpt.py "extract all html headers from a webpage, translate to Spanish and save result into html file" "extract-translate-headers.py"

# Example #2 from "Python Automation with ChatGPT" demonstration
python python-chatgpt.py "go through files in Downloads folder, check their dates and if they are older than 30 days, move them to a folder called to_delete" "clean-downloads.py"
```

Example Response in raw `json`:

```json
{'id': 'cmpl-.....', 'object': 'text_completion', 'created': 1682794373, 'model': 'text-davinci-003', 'choices': [{'text': '\n\n# This is a Python script to print "Hello World"\n\nprint("Hello World!")', 'index': 0, 'logprobs': None, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 7, 'completion_tokens': 22, 'total_tokens': 29}}
```

### Translate headers of a webpage

```sh
python extract-translate-headers.py
# If you get an error like AttributeError: 'NoneType' object has no attribute 'group'
# try to upgrade the googletrans library with:
# pip install --upgrade googletrans==4.0.0-rc1
```

### Clean up Downloads Folder

```sh
python clean-downloads.py
```

## Acknowledgements

- [Python Automation with ChatGPT](https://www.youtube.com/watch?v=w-X_EQ2Xva4) by TechWorld with Nana
  - [python-automation-chatgpt repository with code](https://gitlab.com/nanuchi/python-automation-chatgpt)
- [Best README Template](https://github.com/othneildrew/Best-README-Template/blob/master/README.md)
