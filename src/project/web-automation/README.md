# Web Automation

Automate website interactions

## Web automation setup

Install requirements, depending playwright or selenium

## Using playwright

Initialization options for virtual environment

```shell
# pip option with virtual environment
python3 -m virtualenv ./venv
source ./venv/bin/activate
pip install --upgrade pip
pip install playwright
playwright install

# Conda Option
conda config --add channels conda-forge
conda config --add channels microsoft
conda install playwright
playwright install
```

## Using Selenium

### Set up

```shell
# pip option with virtual environment
python3 -m virtualenv ./venv
source ./venv/bin/activate
pip install selenium

# Conda Option
conda install conda-forge::selenium
```

### Using Selenium with Existing Firefox Browser

- Download the [latest geckodriver](https://github.com/mozilla/geckodriver/releases)
  and put it in path
- Close all Firefox instances
- Start Firefox with `firefox --marionette`
  or if using flatpak `flatpak run org.mozilla.firefox --marionette`
- Run Selenium script to reuse Firefox instance
