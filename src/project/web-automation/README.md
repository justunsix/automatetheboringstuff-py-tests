# Metadata

Gather metadata on movies.

## Web automation setup

Install requirements, depending playwright or selenium

## Using playwright

Initialization options in virtual environment

```shell
# Pip
pip install --upgrade pip
pip install playwright
playwright install

# Conda
conda config --add channels conda-forge
conda config --add channels microsoft
conda install playwright
playwright install
```

## Using Selenium

### Set up

```shell
# Pip
pip install selenium

# Conda
conda install conda-forge::selenium
```

### Using Selenium with Existing Firefox Browser

- Download the [latest geckodriver](https://github.com/mozilla/geckodriver/releases)
  and put it in path
- Close all Firefox instances
- Start Firefox with `firefox --marionette`
  or if using flatpak `flatpak run org.mozilla.firefox --marionette`
- Run Selenium script to reuse Firefox instance
