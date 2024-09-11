# Python and Data Science

Following [Doing Data Science in Visual Studio Code with Python](https://code.visualstudio.com/docs/datascience/overview)

## Built With

Prerequisites needed to run project.

- [Python 3](https://www.python.org/)

## Getting Started

For the commands below use `python` or `python3` depending on your system's python binary.

### Using Python

```sh
# Install dependencies in a virtual environment
python -m venv ./venv
# Activate virtual environment
./venv/Scripts/activate
# or in PowerShell
# ./venv/Scripts/Activate
pip install -r requirements.txt
```

### Using Python with conda

Option install [conda](https://conda.io/projects/conda/en/latest/index.html)

- May be easier for Windows users to use Anaconda distribution since it bundles many packages
- miniconda is a smaller version with fewer packages, if not sure, use conda 

```sh
# Create a new environment using requirements.txt file with packages
# where "data-science" is the name of the environment
conda create --name "data-science" --file requirements.txt --yes
# Activate the environment
conda activate "data-science"
```

- On Windows, in case of error like `CondaVerificationError: The package for tensorflow ...` or `InvalidArchiveError("Error with archive ...` follow these steps [to remove Windows' default max path limit](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/The-Windows-10-default-path-length-limitation-MAX-PATH-is-256-characters.html). The issue is caused by packages in Windows being in very long paths due to multiple nested folders.
- If using an integrated development environment (IDE), start the IDE and you may have to select the appropriate environment
  - For VS Code, activate the environment in the command line and start `code` from the command line. Use the `Python: Select Interpreter` command to [select the environment](https://code.visualstudio.com/docs/datascience/jupyter-notebooks#_setting-up-your-environment). Select the directory of the appropriate environment.

### Run

- Open `exploration.ipynb`
